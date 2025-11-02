FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema necessárias para algumas bibliotecas Python
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Cria o diretório para dados de tracking
RUN mkdir -p tracking_data

# Expõe a porta (Railway usará a variável PORT)
EXPOSE 5000

# Comando de start - Railway sempre define PORT, então usamos gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT app:app

