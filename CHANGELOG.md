# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [v1.0.0] - 2025-09-25

### ✨ Adicionado

#### Interface Web
- Interface web moderna e responsiva
- Upload de arquivos SVG via drag & drop
- Seleção visual de áreas clicáveis com mouse
- Configuração de URLs para cada área
- Preview em tempo real das áreas selecionadas
- Download automático do SVG modificado
- Feedback visual com mensagens de status

#### Funcionalidades Core
- Processamento de arquivos SVG com validação
- Geração de links no formato correto (`href` simples)
- Suporte a elementos `<title>` para acessibilidade
- Áreas clicáveis transparentes com cursor pointer
- Abertura de links em nova aba (`target="_blank"`)

#### Integração com Banco de Dados
- Geração de SVG otimizado para armazenamento
- Recuperação e download de SVG completo do banco
- Interface dedicada para testar conteúdo do banco
- Formato otimizado para queries SQL

#### Docker & DevOps
- Dockerização completa da aplicação
- Configuração para desenvolvimento com hot reload
- Configuração para produção com Nginx
- Scripts de automação (`start.sh`, `Makefile`)
- Variáveis de ambiente configuráveis
- Volumes persistentes para uploads

#### Documentação
- README.md completo com instruções
- Guia de uso passo a passo (COMO_USAR.md)
- Documentação Docker (DOCKER_SETUP.md)
- Instruções para GitHub Copilot
- Arquivo de exemplo SVG para testes

#### Tecnologias
- **Backend**: Python 3.11 + Flask + lxml
- **Frontend**: HTML5 + CSS3 + JavaScript vanilla
- **Container**: Docker + Docker Compose
- **Proxy**: Nginx (opcional)
- **Controle de Versão**: Git com versionamento semântico

### 🔧 Técnico

#### Formato dos Links SVG
```xml
<a href="https://example.com" target="_blank" data-clickable-area="true">
    <title>Link para https://example.com</title>
    <rect x="100" y="50" width="200" height="100" 
          fill="transparent" stroke="none" style="cursor: pointer;"/>
</a>
```

#### Estrutura do Projeto
```
svg-clickable-areas/
├── 🐳 Docker
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.override.yml
│   ├── docker-compose.prod.yml
│   └── nginx.conf
├── 🚀 Scripts
│   ├── start.sh
│   ├── Makefile
│   └── .env
├── 🎯 Aplicação
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/index.html
│   └── uploads/
└── 📝 Documentação
    ├── README.md
    ├── COMO_USAR.md
    ├── DOCKER_SETUP.md
    └── CHANGELOG.md
```

#### Rotas da API
- `GET /` - Interface web principal
- `POST /upload` - Upload e validação de arquivos SVG
- `POST /add_clickable_area` - Adicionar áreas clicáveis (download)
- `POST /add_clickable_area_for_db` - Processar SVG para banco
- `POST /generate_complete_svg_from_db` - Gerar SVG completo do banco
- `GET /download/<filename>` - Download de arquivos

### 🎯 Características

- ✅ Interface intuitiva e moderna
- ✅ Processamento seguro de SVG
- ✅ Links compatíveis com todos os navegadores
- ✅ Suporte completo a banco de dados
- ✅ Ambiente Docker pronto para produção
- ✅ Scripts de automação
- ✅ Documentação completa
- ✅ Código bem estruturado e comentado

---

## Versões Futuras

### [v1.1.0] - Planejado
- [ ] Suporte a áreas circulares e poligonais
- [ ] Editor SVG integrado
- [ ] API REST para integração externa
- [ ] Histórico de modificações
- [ ] Exportação para outros formatos

### [v1.2.0] - Planejado  
- [ ] Batch processing de múltiplos arquivos
- [ ] Interface administrativa
- [ ] Métricas e analytics
- [ ] Temas personalizáveis
- [ ] Suporte a plugins

---

## Formato das Versões

- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Novas funcionalidades mantendo compatibilidade
- **PATCH**: Correções de bugs mantendo compatibilidade

## Links

- [Repositório](.) 
- [Issues](./issues)
- [Documentação](./README.md)