# 🚀 Deploy no Render - SVG Clickable Areas

## 📋 Pré-requisitos

1. **Conta no Render**: https://render.com
2. **Repositório GitHub**: Código deve estar no GitHub
3. **Arquivos necessários**: ✅ Todos criados

## 🔧 Arquivos de Deploy Criados

### `Procfile`
```
web: gunicorn app:app
```

### `runtime.txt`  
```
python-3.11.0
```

### `requirements.txt` (atualizado)
```
Flask==2.3.3
Werkzeug==2.3.7
lxml==4.9.3
Pillow==10.0.1
gunicorn==21.2.0
```

## 🚀 Passo a Passo para Deploy

### 1. **Preparar Repositório**
```bash
# Commitar arquivos de deploy
git add .
git commit -m "feat: Arquivos para deploy no Render"
git push origin main
```

### 2. **Criar Web Service no Render**

1. Acesse https://render.com
2. Clique em **"New +"** → **"Web Service"**
3. Conecte seu repositório GitHub
4. Configure:
   - **Name**: `svg-clickable-areas`
   - **Environment**: `Python 3`
   - **Build Command**: *(deixe vazio - automático)*
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free` (para teste)

### 3. **Variáveis de Ambiente** (opcional)
```
FLASK_DEBUG=0
FLASK_ENV=production
```

### 4. **Deploy Automático**
- Render detectará automaticamente:
  - `requirements.txt` → Instala dependências
  - `runtime.txt` → Python 3.11
  - `Procfile` → Comando de inicialização

## 🌐 Após Deploy

- **URL**: `https://svg-clickable-areas-XXXX.onrender.com`
- **Status**: Monitorar no dashboard do Render
- **Logs**: Disponíveis no painel de controle

## ⚡ Funcionalidades no Render

✅ **Upload PNG/SVG**: Funciona normalmente
✅ **Conversão PNG→SVG**: Pillow instalado
✅ **Áreas clicáveis**: Interface completa
✅ **INSERT SQL**: Download de arquivos
✅ **Logo Pathfind**: Arquivos estáticos servidos

## 🔧 Solução de Problemas

### Erro de Build:
- Verificar `requirements.txt`
- Logs no painel Render

### Erro de Memória:
- Upgradar para plano pago
- Otimizar processamento de imagens

### Arquivos não servidos:
- Render serve automaticamente arquivos estáticos
- Rota `/static/` configurada no Flask

## 💡 Dicas Importantes

1. **Primeiro deploy**: Pode demorar 5-10 minutos
2. **Auto-deploy**: Ativa ao fazer push no GitHub
3. **Free tier**: Dorme após 15min inativo
4. **Upgrade**: Plano pago para produção ($7/mês)

## 🎯 Próximos Passos

1. Commitar arquivos de deploy
2. Push para GitHub
3. Configurar no Render
4. Testar aplicação online
5. Compartilhar URL!