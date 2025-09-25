# Como Usar o SVG Clickable Areas

## 📚 Guia Passo a Passo

### 1. Iniciando a Aplicação

1. Abra o terminal no VS Code
2. Execute a task "Run SVG Clickable Areas App" ou execute:
   ```bash
   python app.py
   ```
3. Acesse http://localhost:5001 no seu navegador

### 2. Fazendo Upload do SVG

1. **Arraste e solte** um arquivo SVG na área de upload OU
2. **Clique** na área de upload para selecionar um arquivo
3. O arquivo será validado e exibido na tela

### 3. Selecionando Áreas Clicáveis

1. **Clique e arraste** sobre a imagem SVG para criar uma seleção retangular
2. Uma borda vermelha tracejada aparecerá mostrando a área selecionada
3. A área mínima é de 10x10 pixels

### 4. Adicionando Links

1. Digite a **URL de destino** no campo "URL de destino"
2. Clique em **"Adicionar Área"**
3. A área aparecerá na lista "Áreas Configuradas"
4. Repita o processo para adicionar mais áreas

### 5. Gerando o SVG Final

1. Clique em **"Gerar SVG com Links"**
2. O sistema processará o arquivo e adicionará os elementos clicáveis
3. Um botão de download aparecerá

### 6. Download do Resultado

1. Clique em **"Baixar SVG Modificado"**
2. O arquivo será baixado com o prefixo "modified_"

## 🔧 Funcionalidades Avançadas

### Gerenciamento de Áreas
- **Visualizar**: Todas as áreas são listadas com suas coordenadas
- **Remover**: Clique no "×" para remover uma área específica
- **Limpar**: Use "Limpar Seleção" para cancelar a seleção atual

### Atalhos e Dicas
- **Arraste e solte**: Funciona com múltiplos arquivos SVG
- **Seleção precisa**: Use zoom do navegador para seleções pequenas
- **URLs válidas**: Sempre inclua http:// ou https://
- **Recomeçar**: Use o botão "Recomeçar" para um novo arquivo

## 🎯 Exemplos de Uso

### Exemplo 1: Banner com Botões
1. Upload de um banner SVG
2. Selecione área do botão "Comprar Agora"
3. Adicione URL: https://loja.exemplo.com/comprar
4. Selecione área do logo
5. Adicione URL: https://exemplo.com

### Exemplo 2: Mapa Interativo
1. Upload de um mapa SVG
2. Selecione área de cada região
3. Adicione URLs específicas para cada região
4. Gere o mapa interativo

### Exemplo 3: Infográfico
1. Upload de infográfico SVG
2. Selecione áreas de estatísticas
3. Adicione links para fontes de dados
4. Crie infográfico clicável

## 🚨 Resolução de Problemas

### Arquivo não carrega
- Verifique se é um arquivo SVG válido
- Tamanho máximo: 16MB
- Encoding deve ser UTF-8

### Área não seleciona
- Clique diretamente na imagem SVG
- Área mínima: 10x10 pixels
- Evite clicar em textos/elementos

### Link não funciona
- Use URLs completas (http:// ou https://)
- Teste a URL em outro navegador
- Verifique caracteres especiais

### Download não inicia
- Permita pop-ups no navegador
- Verifique se há áreas configuradas
- Tente gerar novamente

## 🔍 Tecnicalidades

### Formato do SVG Modificado
O sistema adiciona elementos `<a>` com retângulos transparentes:

```xml
<a xmlns:xlink="http://www.w3.org/1999/xlink" 
   xlink:href="URL_DESTINO" 
   data-clickable-area="true">
  <rect x="100" y="50" width="200" height="100" 
        fill="transparent" 
        stroke="none" 
        style="cursor: pointer;"/>
</a>
```

### Compatibilidade
- ✅ Navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ Dispositivos móveis
- ✅ Leitores de tela (acessibilidade)
- ✅ Impressão (áreas são invisíveis)
