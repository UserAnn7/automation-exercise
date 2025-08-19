# Use an official slim Python base image
FROM python:3.11-slim

# Install system dependencies (including Java for Allure)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    unzip \
    gnupg \
    default-jre \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libxshmfence1 \
    libgtk-3-0 \
    libgbm-dev \
    libx11-xcb1 \
    xvfb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# (Optional) Set JAVA_HOME for Allure explicitly
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Allure CLI using curl
ENV ALLURE_VERSION=2.27.0
RUN curl -L -o allure.tgz https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz && \
    tar -xzf allure.tgz && \
    mv allure-${ALLURE_VERSION} /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    rm allure.tgz

# Install Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Configure Poetry and install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install

# Install missing system dependencies for Playwright browsers
RUN apt-get update && apt-get install -y \
        libnss3 libatk-bridge2.0-0 libxss1 libasound2 \
        libxshmfence1 libgtk-3-0 libgbm-dev libx11-xcb1 \
        fonts-liberation libappindicator3-1 \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright browsers
RUN python -m playwright install

# Make test script executable
RUN chmod +x run_tests.sh

# Default command: run tests
CMD ["./run_tests.sh"]