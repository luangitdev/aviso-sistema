#!/bin/bash

# Script de inicialização da aplicação SVG Clickable Areas
# Uso: ./start.sh [dev|prod|stop|logs|status]

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════╗"
    echo "║              SVG Clickable Areas                 ║"
    echo "║          Docker Container Manager                ║"
    echo "╚══════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_usage() {
    echo -e "${YELLOW}Uso: $0 [comando]${NC}"
    echo ""
    echo "Comandos disponíveis:"
    echo "  dev     - Iniciar em modo desenvolvimento (padrão)"
    echo "  prod    - Iniciar em modo produção"
    echo "  stop    - Parar todos os containers"
    echo "  logs    - Visualizar logs em tempo real"
    echo "  status  - Verificar status dos containers"
    echo "  clean   - Limpar containers e volumes"
    echo "  shell   - Acessar shell do container"
    echo "  test    - Testar se a aplicação está funcionando"
    echo "  help    - Mostrar esta ajuda"
}

check_docker() {
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}❌ Docker não está instalado!${NC}"
        exit 1
    fi

    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}❌ Docker Compose não está instalado!${NC}"
        exit 1
    fi
}

start_dev() {
    echo -e "${GREEN}🚀 Iniciando aplicação em modo desenvolvimento...${NC}"
    docker-compose up --build
}

start_prod() {
    echo -e "${GREEN}🚀 Iniciando aplicação em modo produção...${NC}"
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
    echo -e "${GREEN}✅ Aplicação iniciada!${NC}"
    echo -e "${BLUE}🌐 Acesse: http://localhost:5001${NC}"
}

stop_app() {
    echo -e "${YELLOW}⏹️ Parando aplicação...${NC}"
    docker-compose down
    echo -e "${GREEN}✅ Aplicação parada!${NC}"
}

show_logs() {
    echo -e "${BLUE}📋 Visualizando logs...${NC}"
    docker-compose logs -f svg-app
}

show_status() {
    echo -e "${BLUE}📊 Status dos containers:${NC}"
    docker-compose ps
    echo ""
    
    if docker-compose ps | grep -q "Up"; then
        echo -e "${GREEN}✅ Aplicação está rodando!${NC}"
        echo -e "${BLUE}🌐 Acesse: http://localhost:5001${NC}"
    else
        echo -e "${RED}❌ Aplicação não está rodando${NC}"
    fi
}

clean_app() {
    echo -e "${YELLOW}🧹 Limpando containers e volumes...${NC}"
    docker-compose down -v
    docker system prune -f
    echo -e "${GREEN}✅ Limpeza concluída!${NC}"
}

access_shell() {
    echo -e "${BLUE}🐚 Acessando shell do container...${NC}"
    docker-compose exec svg-app bash
}

test_app() {
    echo -e "${BLUE}🧪 Testando aplicação...${NC}"
    if curl -s http://localhost:5001 > /dev/null; then
        echo -e "${GREEN}✅ Aplicação funcionando!${NC}"
        echo -e "${BLUE}🌐 URL: http://localhost:5001${NC}"
    else
        echo -e "${RED}❌ Aplicação não está respondendo${NC}"
        echo "Verifique os logs com: $0 logs"
    fi
}

# Função principal
main() {
    print_header
    check_docker
    
    case "${1:-dev}" in
        "dev"|"development")
            start_dev
            ;;
        "prod"|"production")
            start_prod
            ;;
        "stop")
            stop_app
            ;;
        "logs")
            show_logs
            ;;
        "status")
            show_status
            ;;
        "clean")
            clean_app
            ;;
        "shell")
            access_shell
            ;;
        "test")
            test_app
            ;;
        "help"|"-h"|"--help")
            print_usage
            ;;
        *)
            echo -e "${RED}❌ Comando inválido: $1${NC}"
            echo ""
            print_usage
            exit 1
            ;;
    esac
}

main "$@"
