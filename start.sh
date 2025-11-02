#!/bin/bash
# Script de start para Railway
# Expande a variável PORT corretamente

PORT=${PORT:-5000}
gunicorn --bind 0.0.0.0:$PORT app:app

