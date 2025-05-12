# Stage 1: Build the Python Application
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy only the files needed for dependency installation
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Run tests to verify the build
RUN pytest integration_test_alert_module.py -v

# Run Ruff linting and Bandit security checks (non-blocking)
RUN ruff check . --exit-zero && \
    bandit -r . || true

# Stage 2: Final Image (Slim, Production-Ready)
FROM python:3.11-slim

WORKDIR /app

# Copy the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

EXPOSE 8080

CMD ["python", "alert_module.py"]