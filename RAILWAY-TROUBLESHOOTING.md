# 🔧 Troubleshooting - Railway.app Deploy

## ❌ Problema: "Deployment Failure" com Build Logs Vazios

Se você está vendo "deployment failure" mas os build logs estão vazios, siga este guia.

## ✅ Verificações Importantes

### 1. **Configuração no Railway Dashboard**

No Railway, verifique:

1. **Variáveis de Ambiente:**
   - Vá em: Settings → Variables
   - Adicione/Verifique:
     - `PORT` (geralmente definido automaticamente pelo Railway)
     - `FLASK_ENV=production` (opcional)
     - `EMAIL_PASSWORD=sua_senha`
     - `EMAIL_FROM=noetikaai@gmail.com`
     - `EMAIL_TO=noetikaai@gmail.com, gabriel.silva@ufabc.edu.br`

2. **Service Settings:**
   - Root Directory: (deixe vazio, ou `/` se necessário)
   - Build Command: (deixe vazio - usa o railway.json)
   - Start Command: (deixe vazio - usa o railway.json)

3. **GitHub Connection:**
   - Certifique-se de que o repositório está conectado corretamente
   - Verifique se está fazendo deploy da branch correta (geralmente `main` ou `master`)

### 2. **Limites do Plano de $5**

O plano Hobby ($5/mês) inclui $5 de uso de recursos:
- Verifique se você não excedeu o limite
- Monitore o uso em: Dashboard → Usage

### 3. **Logs Alternativos**

Se os build logs estão vazios, tente:

1. **Deployment Logs:**
   - Vá em: Deployments → Clique no deployment que falhou
   - Procure por logs de erro

2. **Service Logs:**
   - Vá em: Service → Logs
   - Veja os logs em tempo real

3. **Explorador de Logs:**
   - Dashboard → Logs
   - Visualize todos os logs do ambiente

### 4. **Arquivos Necessários**

Certifique-se de que estes arquivos estão no repositório:

✅ `Procfile` - Define o comando de start
✅ `railway.json` - Configuração do Railway
✅ `requirements.txt` - Dependências Python
✅ `runtime.txt` - Versão do Python (opcional)
✅ `backend.py` - Arquivo principal da aplicação

### 5. **Teste Local**

Antes de fazer deploy, teste localmente:

```bash
# Instale dependências
pip install -r requirements.txt

# Teste o comando de produção
waitress-serve --host=0.0.0.0 --port=5000 backend:app
```

Se funcionar localmente, o problema é específico do Railway.

## 🔄 Soluções Alternativas

### Opção 1: Usar Railway CLI

1. Instale o Railway CLI:
   ```bash
   npm i -g @railway/cli
   ```

2. Faça login:
   ```bash
   railway login
   ```

3. Faça deploy:
   ```bash
   railway up
   ```

Isso pode dar mais informações de erro.

### Opção 2: Criar Novo Service

Às vezes é melhor criar um novo service:

1. No Railway Dashboard: New → New Project
2. Conecte o repositório GitHub novamente
3. Configure variáveis de ambiente
4. Faça deploy

### Opção 3: Usar Render.com como Alternativa

Se o Railway continuar com problemas, considere:
- Render.com (similar ao Railway)
- Heroku (clássico, mas requer cartão de crédito)
- Fly.io (opção gratuita)

## 📞 Contatar Suporte Railway

Se nada funcionar:

1. Acesse: https://railway.app/discord
2. Ou abra um ticket em: support@railway.app
3. Forneça:
   - Link do seu repositório
   - Screenshot dos logs
   - Descrição do problema

## ✅ Checklist Final

Antes de tentar novamente:

- [ ] Todos os arquivos estão commitados no GitHub
- [ ] `Procfile` está presente na raiz
- [ ] `railway.json` está presente na raiz
- [ ] `requirements.txt` está atualizado
- [ ] Variáveis de ambiente configuradas no Railway
- [ ] Testado localmente com sucesso
- [ ] Verificado limite de uso do plano ($5)

## 🎯 Arquivos de Configuração

### Procfile
```
web: waitress-serve --host=0.0.0.0 --port=$PORT backend:app
```

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "pip install -r requirements.txt"
  },
  "deploy": {
    "startCommand": "waitress-serve --host=0.0.0.0 --port=$PORT backend:app",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

