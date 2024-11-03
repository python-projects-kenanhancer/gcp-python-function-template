#!/bin/bash

set -e

# Navigate to the project directory
cd "{{ cookiecutter.project_slug }}"

# Export requirements.txt from Poetry into the function directory
poetry export -f requirements.txt --without-hashes -o function/requirements.txt

# Navigate to the terraform directory
cd terraform

# Initialize Terraform
terraform init

# Apply the Terraform configuration
terraform apply -auto-approve

# Return to the original directory
cd ../..
