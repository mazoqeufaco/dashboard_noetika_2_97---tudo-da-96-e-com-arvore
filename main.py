#!/usr/bin/env python3
"""
Entry point for Railway deployment
This file is detected automatically by Railpack
"""
import os

# Importa e executa o backend
from backend import app

if __name__ == '__main__':
    import sys
    
    # Obtém a porta da variável de ambiente PORT (usado pelo Railway, Heroku, etc.)
    # ou usa 5000 como padrão
    port = int(os.getenv('PORT', '5000'))
    
    # Verifica se é desenvolvimento ou produção
    # Railway e outras plataformas geralmente definem PORT, então assumimos produção se PORT estiver definido
    is_production = (os.getenv('FLASK_ENV') == 'production' or 
                    os.getenv('ENVIRONMENT') == 'production' or
                    os.getenv('PORT') is not None)
    
    if is_production:
        # Produção: usa Waitress (servidor WSGI)
        from waitress import serve
        print("🚀 Starting Noetika Tracking Backend (PRODUCTION)...")
        print(f"📊 Server running at http://0.0.0.0:{port}")
        print("💾 Data will be saved to: tracking_data")
        print("✅ Using Waitress WSGI server (production-ready)\n")
        serve(app, host='0.0.0.0', port=port, threads=4)
    else:
        # Desenvolvimento: usa servidor embutido do Flask
        print("🚀 Starting Noetika Tracking Backend (DEVELOPMENT)...")
        print(f"📊 Server running at http://localhost:{port}")
        print("💾 Data will be saved to: tracking_data")
        print("\n⚠️  WARNING: Development server - not for production!")
        print("   For production, set: FLASK_ENV=production")
        print("   Or use: waitress-serve --host=0.0.0.0 --port=5000 backend:app\n")
        app.run(debug=True, host='0.0.0.0', port=port)

