#!/usr/bin/env python3
"""
Entry point for Railway deployment - Flask app
Railpack detects this automatically for Flask projects
"""
from backend import app

# Railway/Railpack will automatically detect Flask and use gunicorn
# This file makes the 'app' object available at the root level

