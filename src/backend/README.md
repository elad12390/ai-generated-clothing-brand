# Backend Service

This directory contains the backend service for the AI Generated Clothing Brand project, implemented using Test-Driven Development (TDD) principles.

## Project Structure

```
backend/
├── api/          # API endpoints and routing
├── core/         # Core business logic and domain models
├── services/     # Business services (trending topics, AI generation, etc.)
├── utils/        # Utility functions and helpers
├── tests/        # Test files following TDD approach
└── main.py       # Main application entry point
```

## TDD Approach

We follow a strict Test-Driven Development approach:

1. **Write tests first** - Before implementing any functionality, we write comprehensive tests
2. **Run tests** - Verify that tests fail (as expected, since implementation doesn't exist yet)
3. **Implement minimal code** - Write just enough code to make the tests pass
4. **Refactor** - Improve code quality while keeping tests passing
5. **Repeat** - Continue the cycle for each new feature

## Running Tests

To run all tests:

```bash
./scripts/run_tests.sh
```

Or manually:

```bash
source .venv/bin/activate
python -m pytest src/backend/tests/ -v
deactivate
```

## Test Organization

- **Unit Tests**: Test individual functions and classes in isolation
- **Integration Tests**: Test interactions between components (marked with `@pytest.mark.integration`)
- **End-to-End Tests**: Test complete workflows (to be added later)

## Current Implementation Status

✅ **Trending Topic Analysis** - Implemented with tests
  - Fetch trending topics from external APIs
  - Filter inappropriate content
  - Select best topic based on relevance

🟨 **AI Design Generation** - Planned (next)
⬜ **Database Management** - Planned
⬜ **Print-on-Demand Integration** - Planned
⬜ **Website Backend** - Planned