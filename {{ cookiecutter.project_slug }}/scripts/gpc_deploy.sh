#!/bin/bash

set -e

# Navigate to the project directory
cd "{{ cookiecutter.project_slug }}"

# Export requirements.txt from Poetry into the function directory
poetry export -f requirements.txt --without-hashes -o function/requirements.txt

# Deploy the function
gcloud functions deploy {{ cookiecutter.function_name }} \
  --entry-point main \
  --runtime python{{ cookiecutter.python_version.replace('.', '') }} \
  --trigger-http \
  --source function \
  --allow-unauthenticated

# Return to the original directory
cd ..
