import os
import re
import socket
import shutil
import subprocess
import time
import pathlib
import signal

import pytest


def _find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.mark.e2e
def test_e2e_generate_and_fetch_image():
    # Require the project's `uv` runner to be available
    uv = shutil.which('uv')
    if not uv:
        pytest.skip("'uv' runner not found in PATH; skipping e2e test")

    port = _find_free_port()
    repo_root = pathlib.Path(__file__).resolve().parents[3]

    # Start the server using the project's runtime so it uses the same venv
    cmd = [uv, 'run', 'uvicorn', 'src.backend.app:app', '--host', '127.0.0.1', '--port', str(port)]
    env = os.environ.copy()

    proc = subprocess.Popen(cmd, cwd=str(repo_root), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        # wait for health endpoint using urllib
        import urllib.request
        import urllib.error
        import json

        base = f'http://127.0.0.1:{port}'
        deadline = time.time() + 15
        health_ok = False
        while time.time() < deadline:
            try:
                with urllib.request.urlopen(f'{base}/api/health', timeout=1.0) as r:
                    if r.status == 200:
                        health_ok = True
                        break
            except Exception:
                pass
            time.sleep(0.2)
        if not health_ok:
            out, err = proc.communicate(timeout=1)
            pytest.fail(f"Server did not start in time. stdout={out!r} stderr={err!r}")

        # Post a generation request (testing mode should be enabled by default in env)
        post_data = json.dumps({'prompt': 'E2E test prompt'}).encode('utf-8')
        req = urllib.request.Request(f'{base}/api/generate', data=post_data, headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=60.0) as r:
                assert r.status == 200
                body = json.load(r)
        except urllib.error.HTTPError as he:
            pytest.fail(f'generate failed: {he.code} {he.read()}')
        assert 'imageUrl' in body

        # Fetch the generated image via the static route
        m = re.search(r'/static/(.+)$', body['imageUrl'])
        assert m
        rel_path = m.group(1)
        fetch_url = f'{base}/static/{rel_path}'
        try:
            with urllib.request.urlopen(fetch_url, timeout=30.0) as r2:
                assert r2.status == 200
        except urllib.error.HTTPError as he:
            pytest.fail(f'Failed to fetch image at {fetch_url}: {he.code}')

        # Ensure file exists on disk and cleanup
        images_dir = repo_root / 'src' / 'backend' / 'data' / 'images'
        abs_path = images_dir / pathlib.Path(rel_path).name
        assert abs_path.exists(), f'Expected image file at {abs_path}'
        try:
            abs_path.unlink()
        except Exception:
            pass

    finally:
        # Tear down the server process
        try:
            proc.send_signal(signal.SIGINT)
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
            proc.wait(timeout=5)
