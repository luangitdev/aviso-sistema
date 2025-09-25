# 🎯 Backlog: Conversão PNG para SVG

## 📋 Épico: Suporte a Imagens PNG
**Objetivo**: Permitir que usuários façam upload de imagens PNG e automaticamente convertam para SVG antes de adicionar áreas clicáveis.

---

## 🏗️ User Stories e Tasks

### 📦 **Epic 1: Infraestrutura de Conversão**

#### **US1.1**: Como usuário, quero fazer upload de arquivos PNG
- **Critérios de Aceitação**:
  - Interface aceita arquivos PNG além de SVG
  - Validação de formato PNG
  - Preview da imagem PNG carregada
  - Feedback visual durante upload

**Tasks**:
- [ ] **T1.1.1**: Atualizar `ALLOWED_EXTENSIONS` para incluir `png`
- [ ] **T1.1.2**: Modificar função `allowed_file()` para aceitar PNG
- [ ] **T1.1.3**: Atualizar validação no frontend (JavaScript)
- [ ] **T1.1.4**: Adicionar preview para imagens PNG
- [ ] **T1.1.5**: Atualizar mensagens de erro para incluir PNG

**Estimativa**: 3 story points  
**Prioridade**: Alta

---

#### **US1.2**: Como sistema, quero converter PNG para SVG automaticamente
- **Critérios de Aceitação**:
  - Conversão preserva dimensões originais
  - Imagem PNG é embutida como base64 no SVG
  - SVG gerado é válido e renderizável
  - Processo é transparente para o usuário

**Tasks**:
- [ ] **T1.2.1**: Pesquisar e escolher biblioteca Python para conversão
  - Opções: Pillow + cairosvg, svglib, reportlab
  - Recomendação: **Pillow** (PIL) para processamento de imagem
- [ ] **T1.2.2**: Implementar função `convert_png_to_svg()`
- [ ] **T1.2.3**: Integrar conversão na rota `/upload`
- [ ] **T1.2.4**: Tratar erros de conversão
- [ ] **T1.2.5**: Otimizar tamanho do SVG gerado

**Estimativa**: 8 story points  
**Prioridade**: Alta

---

### 🎨 **Epic 2: Interface de Usuário**

#### **US2.1**: Como usuário, quero uma interface unificada para PNG e SVG
- **Critérios de Aceitação**:
  - Mesmo fluxo para PNG e SVG
  - Indicação visual do tipo de arquivo
  - Processo de conversão transparente
  - Feedback durante conversão

**Tasks**:
- [ ] **T2.1.1**: Atualizar texto da interface para mencionar PNG
- [ ] **T2.1.2**: Adicionar indicador de tipo de arquivo
- [ ] **T2.1.3**: Implementar loader durante conversão
- [ ] **T2.1.4**: Atualizar instruções de uso
- [ ] **T2.1.5**: Adicionar tooltips explicativos

**Estimativa**: 5 story points  
**Prioridade**: Média

---

#### **US2.2**: Como usuário, quero ver o resultado da conversão
- **Critérios de Aceitação**:
  - Preview do SVG gerado a partir do PNG
  - Comparação lado a lado (opcional)
  - Informações sobre a conversão
  - Possibilidade de ajustar configurações

**Tasks**:
- [ ] **T2.2.1**: Implementar preview do SVG convertido
- [ ] **T2.2.2**: Mostrar informações da conversão (tamanho, dimensões)
- [ ] **T2.2.3**: Adicionar opção de ajustar qualidade/tamanho
- [ ] **T2.2.4**: Implementar zoom no preview

**Estimativa**: 5 story points  
**Prioridade**: Baixa

---

### ⚙️ **Epic 3: Otimização e Performance**

#### **US3.1**: Como sistema, quero otimizar o processo de conversão
- **Critérios de Aceitação**:
  - Conversão rápida (< 5 segundos para imagens típicas)
  - Uso eficiente de memória
  - SVG gerado otimizado
  - Suporte a diferentes resoluções

**Tasks**:
- [ ] **T3.1.1**: Implementar redimensionamento automático para imagens grandes
- [ ] **T3.1.2**: Otimizar encoding base64
- [ ] **T3.1.3**: Implementar cache de conversões
- [ ] **T3.1.4**: Adicionar compressão de imagem
- [ ] **T3.1.5**: Configurar timeouts apropriados

**Estimativa**: 8 story points  
**Prioridade**: Média

---

#### **US3.2**: Como usuário, quero controlar a qualidade da conversão
- **Critérios de Aceitação**:
  - Opções de qualidade (alta, média, baixa)
  - Preview em tempo real das mudanças
  - Informação sobre tamanho do arquivo
  - Configurações persistentes

**Tasks**:
- [ ] **T3.2.1**: Implementar configurações de qualidade
- [ ] **T3.2.2**: Adicionar slider de qualidade na interface
- [ ] **T3.2.3**: Mostrar tamanho estimado do arquivo
- [ ] **T3.2.4**: Salvar preferências do usuário

**Estimativa**: 5 story points  
**Prioridade**: Baixa

---

## 🔧 Implementação Técnica

### **Dependências Necessárias**
```python
# Adicionar ao requirements.txt
Pillow==10.0.1          # Processamento de imagens
base64                  # Já incluído no Python
```

### **Estrutura da Conversão**
```python
def convert_png_to_svg(png_path, quality='high'):
    """
    Converte PNG para SVG embutindo a imagem como base64
    """
    from PIL import Image
    import base64
    
    # 1. Carregar imagem PNG
    # 2. Redimensionar se necessário
    # 3. Converter para base64
    # 4. Criar SVG wrapper
    # 5. Retornar SVG válido
```

### **Formato SVG de Saída**
```xml
<svg xmlns="http://www.w3.org/2000/svg" 
     width="800" height="600" viewBox="0 0 800 600">
  <image href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..." 
         width="800" height="600" x="0" y="0"/>
  <!-- Áreas clicáveis serão adicionadas aqui -->
</svg>
```

---

## 📊 Roadmap de Implementação

### **Sprint 1** (1 semana)
- ✅ T1.1.1 - T1.1.5: Suporte básico a PNG
- ✅ T1.2.1 - T1.2.2: Implementação da conversão

### **Sprint 2** (1 semana)  
- ✅ T1.2.3 - T1.2.5: Integração completa
- ✅ T2.1.1 - T2.1.3: Interface atualizada

### **Sprint 3** (1 semana)
- ✅ T2.1.4 - T2.1.5: Melhorias UX
- ✅ T3.1.1 - T3.1.2: Otimizações básicas

### **Sprint 4** (1 semana) - Opcional
- ✅ T2.2.1 - T2.2.4: Features avançadas
- ✅ T3.2.1 - T3.2.4: Controles de qualidade

---

## 🎯 Critérios de Aceite do Épico

### **MVP (Mínimo Viável)**
- [x] Upload de PNG funcional
- [x] Conversão automática PNG → SVG
- [x] Áreas clicáveis funcionando no SVG convertido
- [x] Interface atualizada com suporte a PNG

### **Completo**
- [ ] Otimizações de performance
- [ ] Controles de qualidade
- [ ] Preview avançado
- [ ] Configurações personalizáveis

---

## 🚨 Riscos e Mitigações

### **Risco 1**: Tamanho do arquivo SVG muito grande
- **Mitigação**: Implementar redimensionamento automático
- **Plano B**: Opções de qualidade configuráveis

### **Risco 2**: Performance lenta para imagens grandes
- **Mitigação**: Implementar processamento assíncrono
- **Plano B**: Limite de tamanho de arquivo

### **Risco 3**: Compatibilidade com diferentes formatos PNG
- **Mitigação**: Usar Pillow que suporta diversos formatos
- **Plano B**: Validação rigorosa de formatos

---

## 📈 Métricas de Sucesso

- **Performance**: Conversão < 5s para imagens até 5MB
- **Qualidade**: SVG gerado mantém qualidade visual
- **Usabilidade**: Fluxo transparente para o usuário
- **Compatibilidade**: Funciona com PNGs típicos (RGB, RGBA)

---

## 🎉 Definição de Pronto

Uma feature está pronta quando:
- [ ] Código implementado e testado
- [ ] Testes unitários passando
- [ ] Interface atualizada
- [ ] Documentação atualizada
- [ ] Commit com mensagem semântica
- [ ] Testado manualmente com diferentes tipos de PNG