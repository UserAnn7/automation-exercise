#!/bin/bash

# Exit on error
set -e

echo "📦 Starting project installation..."

# STEP 1: Check for Poetry
if ! command -v poetry &> /dev/null
then
    echo "❌ Poetry is not installed. Installing Poetry..."
    brew install poetry
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "✅ Poetry is installed"
fi

# STEP 2: Install dependencies
echo "📦 Installing Python dependencies with Poetry..."
poetry install

# STEP 3: Activating env
#echo "Activating env"
#poetry env activate

# STEP 4: Install Playwright browsers
echo "🌐 Installing Playwright browsers..."
poetry run playwright install --with-deps

# STEP 5: Installing Allure
echo "📦 Installing Allure..."
brew install allure

echo "✅ Installation is complete!"