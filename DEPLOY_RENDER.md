# 🚀 Deploy no Render - SVG Clickable Areas
3. Configure:
   - **Name**: `svg-avisosistema`
   - **Environment**: `Python 3` 📋 Pré-requisitos

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
python-3.11.9
```

### `requirements.txt` (atualizado)
```
Flask==3.0.0
Werkzeug==3.0.1
lxml==5.1.0
Pillow==10.4.0
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
   - **Name**: `svg-avisosistema`
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh` *(ou deixe vazio para automático)*
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

- **URL**: `https://svg-avisosistema-XXXX.onrender.com`
- **Status**: Monitorar no dashboard do Render
- **Logs**: Disponíveis no painel de controle

## ⚡ Funcionalidades no Render

✅ **Upload PNG/SVG**: Funciona normalmente
✅ **Conversão PNG→SVG**: Pillow instalado
✅ **Áreas clicáveis**: Interface completa
✅ **INSERT SQL**: Download de arquivos
✅ **Logo Pathfind**: Arquivos estáticos servidos

## 🔧 Solução de Problemas

### ❌ Erro de Build (KeyError: '__version__'):
**Causa**: Incompatibilidade de versões ou Python muito novo
**Solução**:
1. Verificar se `runtime.txt` tem `python-3.11.9`
2. Verificar se `requirements.txt` tem versões atualizadas
3. Fazer novo commit e push
4. Tentar redeploy no Render

### ❌ Erro "Getting requirements to build wheel":
**Causa**: Dependências incompatíveis com Python 3.13+
**Solução**:
1. Usar Python 3.11.9 (já configurado)
2. Versões testadas das dependências (já configurado)
3. Clear build cache no Render

### ❌ Erro de Memória:
- Upgradar para plano pago
- Otimizar processamento de imagens

### ❌ Arquivos não servidos:
- Render serve automaticamente arquivos estáticos
- Rota `/static/` configurada no Flask

### 🔄 Forçar Rebuild:
1. No Render Dashboard
2. **Manual Deploy** → **Clear build cache**
3. **Deploy latest commit**

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