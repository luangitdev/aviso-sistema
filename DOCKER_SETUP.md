# 🐳 Docker Quick Start Guide - SVG Clickable Areas

## 🚀 **Como Executar (3 Formas Simples):**

### **1. Script Automático (Recomendado):**
```bash
cd /home/luan/script/svg

# Modo desenvolvimento (com hot reload)
./start.sh dev

# Modo produção 
./start.sh prod

# Ver status
./start.sh status

# Ver logs em tempo real
./start.sh logs

# Parar aplicação
./start.sh stop
```

### **2. Usando Makefile:**
```bash
make dev      # Desenvolvimento
make prod     # Produção
make logs     # Ver logs
make status   # Status
make clean    # Limpar tudo
```

### **3. Docker Compose direto:**
```bash
# Desenvolvimento
docker-compose up --build

# Background
docker-compose up -d

# Parar
docker-compose down
```

## 🌐 **Acessar a Aplicação:**

**URL:** http://localhost:5001

## 🎯 **Funcionalidades Implementadas:**

### ✅ **Interface Web Completa:**
- Upload drag & drop de arquivos SVG
- Seleção visual de áreas clicáveis
- Configuração de URLs para cada área
- Preview em tempo real
- Download automático do SVG modificado

### ✅ **Suporte a Banco de Dados:**
- Gerar SVG específico para armazenamento
- Recuperar e baixar SVG completo do banco
- Formato otimizado para queries

### ✅ **Links no Formato Correto:**
```xml
<a href="https://google.com" target="_blank" data-clickable-area="true">
    <title>Link para https://google.com</title>
    <rect x="53.0" y="79.0" width="116.0" height="42.0" 
          fill="transparent" stroke="none" style="cursor: pointer;"/>
</a>
```

## 🔧 **Comandos Úteis:**

```bash
# Ver logs da aplicação
./start.sh logs

# Testar se está funcionando
./start.sh test

# Acessar shell do container
./start.sh shell

# Ver ajuda completa
./start.sh help

# Limpar tudo e recomeçar
./start.sh clean
make clean
```

## 📁 **Estrutura do Projeto:**

```
/home/luan/script/svg/
├── 🐳 Docker Files
│   ├── Dockerfile                    # Imagem da aplicação
│   ├── docker-compose.yml            # Configuração principal
│   ├── docker-compose.override.yml   # Desenvolvimento
│   ├── docker-compose.prod.yml       # Produção
│   ├── nginx.conf                    # Proxy reverso (opcional)
│   └── .dockerignore                 # Arquivos ignorados
│
├── 🚀 Scripts de Execução
│   ├── start.sh                      # Script principal
│   ├── Makefile                      # Comandos make
│   └── .env                          # Variáveis ambiente
│
├── 🎯 Aplicação
│   ├── app.py                        # Flask app principal
│   ├── requirements.txt              # Dependências Python
│   ├── templates/index.html          # Interface web
│   └── uploads/                      # Arquivos temporários
│
└── 📝 Documentação
    ├── README.md                     # Documentação completa
    ├── COMO_USAR.md                  # Guia de uso
    └── exemplo.svg                   # Arquivo de teste
```

## 🎉 **Teste Rápido:**

1. **Execute:** `./start.sh dev`
2. **Acesse:** http://localhost:5001
3. **Upload:** Use o arquivo `exemplo.svg` incluído
4. **Selecione área** sobre um botão (clique e arraste)
5. **Adicione URL:** https://google.com
6. **Gere SVG** e teste no navegador

## 🔍 **Verificação Final:**

```bash
# Status atual
./start.sh status

# Output esperado:
# ✅ Aplicação está rodando!
# 🌐 Acesse: http://localhost:5001
```

## 📞 **Suporte:**

Se encontrar problemas:

1. **Verificar logs:** `./start.sh logs`
2. **Reiniciar:** `./start.sh stop && ./start.sh dev`
3. **Limpar cache:** `./start.sh clean && ./start.sh dev`

---

**🎯 RESULTADO:** Sua aplicação SVG Clickable Areas está 100% funcional via Docker com interface moderna, suporte a banco de dados e links em formato correto! 🚀
