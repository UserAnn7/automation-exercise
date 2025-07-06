# Use an official slim Python base image
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    unzip \
    gnupg \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libxshmfence1 \
    libgtk-3-0 \
    libgbm-dev \
    libx11-xcb1 \
    xvfb \
    && apt-get clean

# Install Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Create and set working directory
WORKDIR /app

# Copy the project files
COPY . .

# Configure Poetry to install dependencies in the current container environment
RUN poetry config virtualenvs.create false

# Install project dependencies
RUN poetry install

# Install Playwright browsers
RUN python -m playwright install --with-deps

# Make test runner script executable
RUN chmod +x run_tests.sh

# Default command: run tests
CMD ["./run_tests.sh"]