#!/bin/bash

echo "Creating Virtual requirement"
python -m venv venv

echo "Activating Virtual Enviroment ..."
source venv/bin/activate

echo "Installing required packages ..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready."