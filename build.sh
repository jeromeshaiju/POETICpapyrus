#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -o errexit  

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
