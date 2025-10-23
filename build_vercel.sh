#!/bin/bash

# Build script for Vercel deployment
echo "Starting Vercel build..."

# Install dependencies
pip install -r requirements.txt

# Create migrations
python manage.py makemigrations --noinput

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear

echo "Build completed successfully!"

