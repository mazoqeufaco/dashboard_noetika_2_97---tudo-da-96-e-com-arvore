#!/usr/bin/env python3
"""
Wrapper para iniciar o servidor no Railway
Lê PORT da variável de ambiente e inicia gunicorn
"""
import os
import subprocess
import sys

# Obtém a porta da variável de ambiente (Railway sempre define isso)
port = os.getenv('PORT', '5000')

# Comando gunicorn
cmd = [
    'gunicorn',
    '--bind', f'0.0.0.0:{port}',
    '--workers', '4',
    '--threads', '2',
    '--timeout', '120',
    'app:app'
]

print(f"🚀 Starting server on port {port}")
print(f"📊 Command: {' '.join(cmd)}")
sys.stdout.flush()

# Executa gunicorn
try:
    subprocess.run(cmd, check=True)
except KeyboardInterrupt:
    print("\n👋 Shutting down gracefully...")
    sys.exit(0)
except Exception as e:
    print(f"❌ Error starting server: {e}")
    sys.exit(1)

