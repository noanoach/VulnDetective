# ----------------------------------------
# Base image - Python 3.10 on Debian
# ----------------------------------------
FROM python:3.10-slim

# ----------------------------------------
# Set environment variables
# ----------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ----------------------------------------
# Install system dependencies
# ----------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        build-essential \
        wget \
        curl \
        ca-certificates \
        libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------------------
# Install huggingface-cli
# ----------------------------------------
RUN pip install --no-cache-dir huggingface_hub

# ----------------------------------------
# Create app directory
# ----------------------------------------
WORKDIR /app

# ----------------------------------------
# Copy project files
# ----------------------------------------
COPY . .

# ----------------------------------------
# Install Python dependencies
# ----------------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# ----------------------------------------
# Clone and build llama.cpp
# ----------------------------------------
RUN git clone https://github.com/ggerganov/llama.cpp && \
    cd llama.cpp && \
    make

# ----------------------------------------
# Declare volume for the model file
# This way, the user can mount their own gemma-2b-it.gguf
# instead of packaging it into the image (because of license restrictions)
# ----------------------------------------
VOLUME ["/app/models"]

# ----------------------------------------
# Set default command
# For example, show help message
# ----------------------------------------
CMD ["python", "analyzer.py", "--help"]
