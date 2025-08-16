#!/bin/bash
# Script to initialize GitHub repository and set up project structure

echo "Initializing AI Generated Clothing Brand project..."

# Create main directories if they don't exist
mkdir -p src/backend
mkdir -p src/frontend
mkdir -p docs
mkdir -p tests

# Initialize git repository
git init

# Create basic files
touch README.md
touch .gitignore

# Add common Python entries to .gitignore
cat > .gitignore << EOF
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Environment variables
.env

# Logs
*.log

# Database
*.db
*.sqlite

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
EOF

# Create initial commit
git add .
git commit -m "Initial commit: Project structure and documentation"

echo "GitHub repository initialized successfully!"
echo "Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add the remote origin: git remote add origin <repository-url>"
echo "3. Push the initial commit: git push -u origin main"