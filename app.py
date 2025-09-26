from flask import Flask, render_template, request, jsonify, send_file
import os
import tempfile
from werkzeug.utils import secure_filename
from lxml import etree
import uuid
import base64
from PIL import Image
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'svg-clickable-areas-secret-key'

# Criar pasta de uploads se não existir
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'svg', 'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_png_to_svg(png_path, quality='high'):
    """
    Converte PNG para SVG embutindo a imagem como base64
    
    Args:
        png_path (str): Caminho para o arquivo PNG
        quality (str): Qualidade da conversão ('high', 'medium', 'low')
        
    Returns:
        str: Conteúdo SVG com a imagem PNG embutida
    """
    try:
        # Abrir imagem PNG
        with Image.open(png_path) as img:
            # Converter para RGB se necessário (remove transparência)
            if img.mode in ('RGBA', 'LA'):
                # Criar fundo branco para transparência
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])  # Usar canal alpha como máscara
                else:
                    background.paste(img)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Redimensionar se necessário baseado na qualidade
            original_size = img.size
            if quality == 'medium' and max(img.size) > 1200:
                img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            elif quality == 'low' and max(img.size) > 800:
                img.thumbnail((800, 800), Image.Resampling.LANCZOS)
            
            # Converter para base64
            buffer = io.BytesIO()
            img.save(buffer, format='PNG', optimize=True)
            img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            # Criar SVG wrapper
            width, height = img.size
            svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     width="{width}" height="{height}" 
     viewBox="0 0 {width} {height}">
  <title>Imagem convertida de PNG</title>
  <image href="data:image/png;base64,{img_base64}" 
         width="{width}" height="{height}" 
         x="0" y="0"/>
</svg>'''
            
            return svg_content
            
    except Exception as e:
        raise Exception(f"Erro na conversão PNG para SVG: {str(e)}")

def is_png_file(filename):
    """
    Verifica se o arquivo é PNG baseado na extensão
    """
    return filename.lower().endswith('.png')

def normalize_url(url):
    """
    Normaliza URLs para garantir que sejam absolutos
    
    Args:
        url (str): URL para normalizar
        
    Returns:
        str: URL normalizado com protocolo
    """
    if not url:
        return url
    
    url = url.strip()
    
    # Se já tem protocolo, retorna como está
    if url.startswith(('http://', 'https://', 'ftp://', 'mailto:', 'tel:')):
        return url
    
    # Se começa com //, adiciona https:
    if url.startswith('//'):
        return 'https:' + url
    
    # Para domínios comuns, adiciona https://
    if any(url.startswith(domain) for domain in [
        'www.', 'google.com', 'facebook.com', 'instagram.com', 'twitter.com',
        'linkedin.com', 'youtube.com', 'github.com', 'stackoverflow.com'
    ]) or ('.' in url and not url.startswith('/')):
        return 'https://' + url
    
    # Para caminhos relativos ou outros casos, mantém como está
    return url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<filename>')
def serve_static(filename):
    """
    Serve arquivos estáticos (imagens, etc.)
    """
    return send_file(filename, as_attachment=False)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Adicionar UUID para evitar conflitos
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Verificar se é PNG e converter para SVG
            if is_png_file(filename):
                print(f"🖼️  Convertendo PNG para SVG: {filename}")
                svg_content = convert_png_to_svg(filepath, quality='high')
                
                # Salvar SVG convertido
                svg_filename = f"{name}_converted_{uuid.uuid4().hex[:8]}.svg"
                svg_filepath = os.path.join(app.config['UPLOAD_FOLDER'], svg_filename)
                
                with open(svg_filepath, 'w', encoding='utf-8') as f:
                    f.write(svg_content)
                
                # Remover PNG original para economizar espaço
                os.remove(filepath)
                
                return jsonify({
                    'success': True,
                    'filename': svg_filename,
                    'content': svg_content,
                    'converted_from_png': True,
                    'message': 'PNG convertido para SVG com sucesso!'
                })
            
            # Processar SVG normal
            else:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse do SVG para verificar se é válido
                parser = etree.XMLParser(recover=True)
                etree.fromstring(content.encode('utf-8'), parser)
                
                return jsonify({
                    'success': True,
                    'filename': filename,
                    'content': content,
                    'converted_from_png': False
                })
                
        except Exception as e:
            # Remover arquivo em caso de erro
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': f'Erro ao processar arquivo: {str(e)}'}), 400
    
    return jsonify({'error': 'Tipo de arquivo não permitido. Apenas arquivos SVG e PNG são aceitos.'}), 400

@app.route('/add_clickable_area', methods=['POST'])
def add_clickable_area():
    """
    Adiciona áreas clicáveis ao SVG no formato correto
    """
    try:
        data = request.get_json()
        filename = data.get('filename')
        areas = data.get('areas', [])
        
        if not filename:
            return jsonify({'error': 'Nome do arquivo não fornecido'}), 400
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'error': 'Arquivo não encontrado'}), 404
        
        # Ler o SVG
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse do SVG
        parser = etree.XMLParser(recover=True)
        root = etree.fromstring(content.encode('utf-8'), parser)
        
        # Namespace SVG
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        
        # Remover áreas clicáveis existentes (se houver)
        existing_areas = root.xpath('.//svg:a[@data-clickable-area="true"]', namespaces=ns)
        for area in existing_areas:
            area.getparent().remove(area)
        
        # Adicionar novas áreas clicáveis no formato correto
        for i, area in enumerate(areas):
            x = float(area['x'])
            y = float(area['y'])
            width = float(area['width'])
            height = float(area['height'])
            url = normalize_url(area['url'])  # Normalizar URL
            
            # Criar elemento <a> SEM namespace xlink
            a_elem = etree.Element('{http://www.w3.org/2000/svg}a')
            a_elem.set('href', url)  # href simples, sem namespace
            a_elem.set('target', '_blank')  # Abrir em nova aba
            a_elem.set('data-clickable-area', 'true')
            
            # Criar elemento <title> para acessibilidade
            title_elem = etree.Element('{http://www.w3.org/2000/svg}title')
            title_elem.text = f'Link para {url}'
            a_elem.append(title_elem)
            
            # Criar retângulo invisível
            rect_elem = etree.Element('{http://www.w3.org/2000/svg}rect')
            rect_elem.set('x', str(x))
            rect_elem.set('y', str(y))
            rect_elem.set('width', str(width))
            rect_elem.set('height', str(height))
            rect_elem.set('fill', 'transparent')
            rect_elem.set('stroke', 'none')
            rect_elem.set('style', 'cursor: pointer;')
            
            a_elem.append(rect_elem)
            root.append(a_elem)
        
        # Converter de volta para string
        modified_svg = etree.tostring(root, encoding='unicode', method='xml')
        
        # Garantir que tenha declaração XML
        if not modified_svg.startswith('<?xml'):
            modified_svg = '<?xml version="1.0" encoding="UTF-8"?>\n' + modified_svg
        
        # Salvar arquivo modificado
        modified_filename = f"modified_{filename}"
        modified_filepath = os.path.join(app.config['UPLOAD_FOLDER'], modified_filename)
        
        with open(modified_filepath, 'w', encoding='utf-8') as f:
            f.write(modified_svg)
        
        return jsonify({
            'success': True,
            'modified_filename': modified_filename,
            'content': modified_svg
        })
    
    except Exception as e:
        return jsonify({'error': f'Erro ao processar SVG: {str(e)}'}), 500

@app.route('/add_clickable_area_for_db', methods=['POST'])
def add_clickable_area_for_db():
    """
    Processa SVG para armazenamento no banco de dados
    Retorna apenas a tag SVG com áreas clicáveis no formato correto
    """
    try:
        data = request.get_json()
        filename = data.get('filename')
        areas = data.get('areas', [])
        
        if not filename:
            return jsonify({'error': 'Nome do arquivo não fornecido'}), 400
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'error': 'Arquivo não encontrado'}), 404
        
        # Ler o SVG
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse do SVG
        parser = etree.XMLParser(recover=True)
        root = etree.fromstring(content.encode('utf-8'), parser)
        
        # Garantir namespace SVG
        if root.tag != '{http://www.w3.org/2000/svg}svg':
            # Se não tem namespace, adicionar
            root.set('xmlns', 'http://www.w3.org/2000/svg')
        
        # Namespace SVG
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        
        # Remover áreas clicáveis existentes (se houver)
        existing_areas = root.xpath('.//svg:a[@data-clickable-area="true"]', namespaces=ns)
        for area in existing_areas:
            area.getparent().remove(area)
        
        # Adicionar novas áreas clicáveis no formato correto
        for i, area in enumerate(areas):
            x = float(area['x'])
            y = float(area['y'])
            width = float(area['width'])
            height = float(area['height'])
            url = normalize_url(area['url'])  # Normalizar URL
            
            # Criar elemento <a> no formato correto
            a_elem = etree.Element('{http://www.w3.org/2000/svg}a')
            a_elem.set('href', url)  # href simples
            a_elem.set('target', '_blank')
            a_elem.set('data-clickable-area', 'true')
            
            # Criar elemento <title> para acessibilidade
            title_elem = etree.Element('{http://www.w3.org/2000/svg}title')
            title_elem.text = f'Link para {url}'
            a_elem.append(title_elem)
            
            # Criar retângulo invisível
            rect_elem = etree.Element('{http://www.w3.org/2000/svg}rect')
            rect_elem.set('x', str(x))
            rect_elem.set('y', str(y))
            rect_elem.set('width', str(width))
            rect_elem.set('height', str(height))
            rect_elem.set('fill', 'transparent')
            rect_elem.set('stroke', 'none')
            rect_elem.set('style', 'cursor: pointer;')
            
            a_elem.append(rect_elem)
            root.append(a_elem)
        
        # Converter para string (apenas a tag SVG, sem declaração XML)
        svg_for_db = etree.tostring(root, encoding='unicode', method='xml')
        
        return jsonify({
            'success': True,
            'svg_content': svg_for_db,
            'message': f'SVG processado para banco com {len(areas)} área(s) clicável(is)'
        })
    
    except Exception as e:
        return jsonify({'error': f'Erro ao processar SVG para banco: {str(e)}'}), 500

@app.route('/generate_complete_svg_from_db', methods=['POST'])
def generate_complete_svg_from_db():
    """
    Gera SVG completo a partir do conteúdo armazenado no banco
    """
    try:
        data = request.get_json()
        svg_content = data.get('svg_content')
        
        if not svg_content:
            return jsonify({'error': 'Conteúdo SVG é obrigatório'}), 400
        
        # Adicionar declaração XML se não existir
        if not svg_content.strip().startswith('<?xml'):
            complete_svg = f'<?xml version="1.0" encoding="UTF-8"?>\n{svg_content}'
        else:
            complete_svg = svg_content
        
        # Criar arquivo temporário
        import time
        filename = f'svg_from_db_{int(time.time())}.svg'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(complete_svg)
        
        return send_file(filepath, as_attachment=True, download_name='svg_completo_do_banco.svg')
        
    except Exception as e:
        return jsonify({'error': f'Erro ao gerar SVG: {str(e)}'}), 500

@app.route('/generate_sql_insert', methods=['POST'])
def generate_sql_insert():
    """
    Gera comando SQL INSERT com o conteúdo SVG embutido
    """
    try:
        data = request.get_json()
        filename = data.get('filename')
        assunto = data.get('assunto', 'COMUNICADO')
        custom_date = data.get('data_criacao')
        
        if not filename:
            return jsonify({'error': 'Nome do arquivo não fornecido'}), 400
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'error': 'Arquivo não encontrado'}), 404
        
        # Ler o SVG
        with open(filepath, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        
        # Extrair apenas a tag SVG (sem declaração XML)
        if svg_content.startswith('<?xml'):
            # Encontrar onde começa a tag <svg>
            svg_start = svg_content.find('<svg')
            if svg_start != -1:
                svg_content = svg_content[svg_start:]
        
        # Escapar aspas simples para SQL
        svg_escaped = svg_content.replace("'", "''")
        
        # Gerar data atual se não fornecida
        from datetime import datetime
        if custom_date:
            data_sql = custom_date
        else:
            data_sql = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Gerar comando SQL INSERT
        sql_insert = f"""INSERT INTO public.avisosistema (assunto, atualizado, aviso, criacao) 
VALUES ('{assunto}', '{data_sql}', '{svg_escaped}', '{data_sql}');"""
        
        # Salvar arquivo SQL
        import time
        sql_filename = f'insert_avisosistema_{int(time.time())}.sql'
        sql_filepath = os.path.join(app.config['UPLOAD_FOLDER'], sql_filename)
        
        with open(sql_filepath, 'w', encoding='utf-8') as f:
            f.write(sql_insert)
        
        return jsonify({
            'success': True,
            'sql_filename': sql_filename,
            'sql_content': sql_insert,
            'message': f'Comando SQL INSERT gerado com sucesso para tabela avisosistema'
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro ao gerar SQL INSERT: {str(e)}'}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(filepath):
            return jsonify({'error': 'Arquivo não encontrado'}), 404
        
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({'error': f'Erro ao baixar arquivo: {str(e)}'}), 500

if __name__ == '__main__':
    # Configuração para Docker e desenvolvimento
    import os
    
    # Obter configurações do ambiente
    debug_mode = os.getenv('FLASK_DEBUG', '1') == '1'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', '5001'))
    
    print(f"🚀 Iniciando aplicação SVG Clickable Areas")
    print(f"🌐 Host: {host}:{port}")
    print(f"🔧 Debug: {debug_mode}")
    print(f"📁 Upload folder: {app.config['UPLOAD_FOLDER']}")
    
    app.run(debug=debug_mode, host=host, port=port)
