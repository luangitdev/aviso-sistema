.PHONY: build up down logs restart clean dev prod shell install

# Comandos para desenvolvimento
dev:
	@echo "🚀 Iniciando aplicação em modo desenvolvimento..."
	docker-compose up --build

build:
	@echo "🔨 Construindo imagem Docker..."
	docker-compose build

up:
	@echo "▶️ Iniciando aplicação..."
	docker-compose up -d

down:
	@echo "⏹️ Parando aplicação..."
	docker-compose down

logs:
	@echo "📋 Visualizando logs..."
	docker-compose logs -f svg-app

restart:
	@echo "🔄 Reiniciando aplicação..."
	docker-compose restart svg-app

# Comandos para produção
prod:
	@echo "🚀 Iniciando aplicação em modo produção..."
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Limpeza
clean:
	@echo "🧹 Limpando containers e volumes..."
	docker-compose down -v
	docker system prune -f

# Acesso ao container
shell:
	@echo "🐚 Acessando shell do container..."
	docker-compose exec svg-app bash

# Instalar dependências
install:
	@echo "📦 Instalando dependências..."
	docker-compose exec svg-app pip install -r requirements.txt

# Status dos containers
status:
	@echo "📊 Status dos containers:"
	docker-compose ps

# Verificar aplicação
test:
	@echo "🧪 Testando aplicação..."
	curl -s http://localhost:5001 > /dev/null && echo "✅ Aplicação funcionando!" || echo "❌ Aplicação não está respondendo"

# Ajuda
help:
	@echo "📖 Comandos disponíveis:"
	@echo "  make dev      - Iniciar em modo desenvolvimento"
	@echo "  make prod     - Iniciar em modo produção"
	@echo "  make build    - Construir imagem"
	@echo "  make up       - Iniciar aplicação (background)"
	@echo "  make down     - Parar aplicação"
	@echo "  make logs     - Ver logs em tempo real"
	@echo "  make restart  - Reiniciar aplicação"
	@echo "  make shell    - Acessar shell do container"
	@echo "  make status   - Ver status dos containers"
	@echo "  make test     - Testar se aplicação está funcionando"
	@echo "  make clean    - Limpar containers e volumes"
	@echo "  make help     - Mostrar esta ajuda"
