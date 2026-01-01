#!/bin/bash

echo "Starting TCP Bot..."
python main.py &

echo "Starting API..."
gunicorn api:app --bind 0.0.0.0:$PORT
