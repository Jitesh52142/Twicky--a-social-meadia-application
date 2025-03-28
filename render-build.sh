#!/bin/bash

# Run migrations before starting the server
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Start the server
gunicorn twiky_project.wsgi:application --bind 0.0.0.0:8000
