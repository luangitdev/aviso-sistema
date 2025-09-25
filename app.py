from flask import Flask, render_template, request, jsonify, send_file
import os
import tempfile
from werkzeug.utils import secure_filename
from lxml import etree
import uuid

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'svg-clickable-areas-secret-key'

# Criar pasta de uploads se não existir
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'svg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

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
        
        # Verificar se é um SVG válido
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse do SVG para verificar se é válido
            parser = etree.XMLParser(recover=True)
            etree.fromstring(content.encode('utf-8'), parser)
            
            return jsonify({
                'success': True,
                'filename': filename,
                'content': content
            })
        except Exception as e:
            os.remove(filepath)
            return jsonify({'error': f'Arquivo SVG inválido: {str(e)}'}), 400
    
    return jsonify({'error': 'Tipo de arquivo não permitido. Apenas arquivos SVG são aceitos.'}), 400

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
            url = area['url']
            
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
            url = area['url']
            
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
