#!/usr/bin/env bash
# Start script for Render
gunicorn twiky_project.wsgi:application --bind 0.0.0.0:$PORT
