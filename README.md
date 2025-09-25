# SVG Clickable Area## 🔧 Instalação

### **Opção 1: Usando Docker (Recomendado) 🐳**

**Pré-requisitos:**
- Docker
- Docker Compose

**Instalação rápida:**
```bash
# Clonar/baixar o projeto
cd svg-clickable-areas

# Iniciar aplicação
./start.sh dev
# ou
make dev
# ou
docker-compose up --build
```

### **Opção 2: Instalação Manual**

**Pré-requisitos:**
- Python 3.7+
- pip (gerenciador de pacotes Python)

**Passos:**
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py
```cação web Python que permite tornar áreas específicas de imagens SVG clicáveis de forma fácil e automatizada.

## 🚀 Funcionalidades

- **Upload de SVG**: Arraste e solte ou selecione arquivos SVG
- **Seleção Visual**: Selecione áreas retangulares diretamente na imagem
- **Adição de Links**: Configure URLs para cada área selecionada
- **Preview em Tempo Real**: Visualize as áreas sendo configuradas
- **Download Automático**: Baixe o SVG modificado com áreas clicáveis
- **Interface Responsiva**: Funciona em desktop e mobile

## 🛠️ Tecnologias

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Processamento SVG**: lxml
- **Interface**: Design responsivo com drag-and-drop

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone ou baixe este projeto
2. Navegue até o diretório do projeto
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### **Com Docker (Recomendado):**

```bash
# Modo desenvolvimento (com hot reload)
./start.sh dev

# Modo produção
./start.sh prod

# Ver logs
./start.sh logs

# Parar aplicação
./start.sh stop

# Ver status
./start.sh status
```

### **Sem Docker:**

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python app.py
```

**Acesse:** http://localhost:5001

3. **Workflow de uso**:
   - Faça upload de um arquivo SVG
   - Clique e arraste para selecionar uma área na imagem
   - Digite a URL de destino
   - Clique em "Adicionar Área"
   - Repita para adicionar mais áreas
   - Clique em "Gerar SVG com Links"
   - Baixe o arquivo modificado

## 📁 Estrutura do Projeto

```
svg-clickable-areas/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── templates/
│   └── index.html        # Interface web
├── uploads/              # Arquivos temporários (criado automaticamente)
└── README.md
```

## 🔍 Como Funciona

1. **Upload**: O arquivo SVG é carregado e validado
2. **Seleção**: JavaScript captura coordenadas da área selecionada
3. **Processamento**: Python usa lxml para inserir elementos `<a>` e `<rect>` no SVG
4. **Download**: Arquivo modificado disponibilizado para download

### Exemplo de SVG Modificado

A aplicação gera links no formato correto para máxima compatibilidade:

```xml
<svg xmlns="http://www.w3.org/2000/svg" ...>
  <!-- Conteúdo original do SVG -->
  
  <!-- Área clicável adicionada no formato correto -->
  <a href="https://exemplo.com" target="_blank" data-clickable-area="true">
    <title>Link para https://exemplo.com</title>
    <rect x="100" y="50" width="200" height="100" 
          fill="transparent" stroke="none" 
          style="cursor: pointer;"/>
  </a>
</svg>
```

#### ✅ **Formato Correto dos Links:**
- `href="URL"` - Atributo href simples (sem namespaces)
- `target="_blank"` - Abre em nova aba
- `<title>` - Texto de acessibilidade
- `cursor: pointer` - Indica área clicável
- `fill="transparent"` - Área invisível mas funcional

## � Usando Docker

### **Comandos básicos:**

```bash
# Script de inicialização (recomendado)
./start.sh dev          # Desenvolvimento
./start.sh prod         # Produção
./start.sh stop         # Parar
./start.sh logs         # Ver logs
./start.sh status       # Status
./start.sh shell        # Acessar container
./start.sh test         # Testar aplicação

# Ou usando Makefile
make dev               # Desenvolvimento
make prod              # Produção
make logs              # Ver logs
make clean             # Limpar tudo

# Ou usando docker-compose diretamente
docker-compose up --build    # Desenvolvimento
docker-compose up -d         # Background
docker-compose down          # Parar
```

### **Vantagens do Docker:**
- ✅ **Ambiente isolado** e consistente
- ✅ **Não precisa instalar** Python localmente
- ✅ **Deploy fácil** em qualquer servidor
- ✅ **Configuração automática** de dependências
- ✅ **Hot reload** em desenvolvimento

## �🗄️ Integração com Banco de Dados

A aplicação oferece funcionalidades específicas para trabalhar com bancos de dados:

### **Gerar SVG para Banco**
1. Processe as áreas clicáveis normalmente
2. Clique em **"Gerar para Banco de Dados"**
3. Copie o conteúdo SVG gerado
4. Armazene apenas a tag `<svg>` no banco

### **Recuperar do Banco**
1. Cole o conteúdo SVG do banco
2. Clique em **"Baixar SVG Completo"**
3. O sistema adiciona a declaração XML automaticamente

### **Vantagens desta Abordagem:**
- **Menor espaço**: Armazena apenas o essencial
- **Flexibilidade**: Fácil de manipular no banco
- **Compatibilidade**: Funciona com qualquer SGBD
- **Performance**: Queries mais rápidas

## 🎨 Características da Interface

- **Design Moderno**: Interface limpa e profissional
- **Feedback Visual**: Indicadores de status e progresso
- **Drag & Drop**: Upload intuitivo de arquivos
- **Seleção Interativa**: Visualização em tempo real das áreas
- **Responsivo**: Adaptável a diferentes tamanhos de tela

## 🔐 Segurança

- Validação de tipo de arquivo (apenas SVG)
- Sanitização de nomes de arquivo
- Limite de tamanho de upload (16MB)
- Parse seguro de XML
- Prevenção de ataques XSS

## 🚨 Limitações

- Apenas áreas retangulares são suportadas
- Requer arquivos SVG válidos
- Áreas clicáveis sobrescrevem as existentes

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆘 Suporte

Se encontrar problemas:

1. Verifique se o arquivo SVG é válido
2. Confirme que as dependências estão instaladas
3. Verifique os logs da aplicação no terminal
4. Certifique-se de que a porta 5000 está disponível

## 🔄 Próximas Funcionalidades

- [ ] Suporte a áreas circulares e poligonais
- [ ] Editor de SVG integrado
- [ ] Histórico de modificações
- [ ] Exportação para diferentes formatos
- [ ] API REST para integração
- [ ] Batch processing de múltiplos arquivos
