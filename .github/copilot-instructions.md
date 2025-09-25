<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# SVG Clickable Areas - Copilot Instructions

Este é um projeto Python Flask para criar áreas clicáveis em imagens SVG.

## Contexto do Projeto
- **Objetivo**: Automatizar a criação de áreas clicáveis em arquivos SVG
- **Tecnologia**: Python Flask com interface web
- **Funcionalidades**: Upload de SVG, seleção visual de áreas, adição de links, download do SVG modificado

## Estrutura do Projeto
- `app.py`: Aplicação Flask principal com rotas para upload, processamento e download
- `templates/index.html`: Interface web completa com JavaScript para interação
- `requirements.txt`: Dependências Python (Flask, lxml, Werkzeug)
- `uploads/`: Diretório para arquivos temporários

## Tecnologias Utilizadas
- **Backend**: Python Flask para API REST
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Processamento SVG**: lxml para manipulação XML
- **Interface**: Design responsivo com drag-and-drop

## Padrões de Código
- Use docstrings em português para funções Python
- Mantenha o código JavaScript limpo e bem comentado
- Tratamento de erros robusto tanto no backend quanto frontend
- Validação de arquivos SVG antes do processamento
- Nomes de variáveis em português quando apropriado

## Funcionalidades Implementadas
1. Upload de arquivos SVG com validação
2. Visualização do SVG na interface web
3. Seleção visual de áreas retangulares com mouse
4. Adição de URLs para cada área selecionada
5. Geração de SVG modificado com elementos `<a>` e `<rect>`
6. Download do arquivo SVG modificado
7. Interface responsiva para mobile e desktop

## Considerações de Segurança
- Validação de tipos de arquivo
- Sanitização de nomes de arquivo
- Limitação de tamanho de upload
- Parse seguro de XML com lxml
