#!/bin/bash

# Ensure migration files are created
python manage.py makemigrations --noinput  

# Force apply migrations
python manage.py migrate --run-syncdb --noinput  

# Collect static files
python manage.py collectstatic --no-input  

# Start the server
gunicorn twiky_project.wsgi:application --bind 0.0.0.0:8000
