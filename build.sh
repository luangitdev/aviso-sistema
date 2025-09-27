#!/bin/bash

# Build script para Render
echo "🚀 Iniciando build customizado..."

# Instalar dependências
echo "📦 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Criar diretórios necessários
echo "📁 Criando diretórios..."
mkdir -p uploads
mkdir -p static

echo "✅ Build concluído!"