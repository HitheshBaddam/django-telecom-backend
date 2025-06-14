# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app/telecom_project

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv or use requirements.txt
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy project files
COPY . /app/

# Run Django server
CMD ["gunicorn", "telecom_project.wsgi:application", "--bind", "0.0.0.0:8000"]


