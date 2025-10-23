#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

# Make migrations (if needed)
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

