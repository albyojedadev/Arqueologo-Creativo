import os
import sys
import json
import argparse
import re
import zipfile
import xml.etree.ElementTree as ET

# Set stdout encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def extract_text_sample(file_path, ext):
    """Extrae de forma segura una muestra de texto de diversos formatos sin alterar el archivo."""
    try:
        if ext in ['.txt', '.md', '.json', '.yaml', '.yml']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read(1500)
        elif ext == '.docx':
            with zipfile.ZipFile(file_path) as z:
                xml_content = z.read('word/document.xml')
                tree = ET.fromstring(xml_content)
                text = ' '.join([''.join([t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]) for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')])
                return text[:1500]
        elif ext == '.doc':
            with open(file_path, 'rb') as f:
                content = f.read().decode('latin-1', errors='ignore')
            strings = re.findall(r'[A-Za-z0-9áéíóúÁÉÍÓÚñÑüÜ\s,.;:\-¿?¡!"\(\)]{4,}', content)
            meaningful = [s for s in strings if len(s.strip()) > 10 and not s.startswith('Normal') and not s.startswith('Heading')]
            return ' '.join(meaningful[:40])[:1500]
    except Exception:
        return ""
    return ""

def scan_vault(target_path, output_json):
    """Escanea la carpeta de forma 100% de solo lectura y genera un inventario estructurado."""
    if not os.path.exists(target_path):
        print(f"❌ Error: Path not found / Ruta no encontrada: {target_path}")
        sys.exit(1)

    print(f"🔍 Iniciando escaneo seguro (Solo Lectura) en: {target_path}")
    
    inventory = {
        'target_path': target_path,
        'total_files': 0,
        'total_size_mb': 0,
        'extensions': {},
        'clusters': {},
        'extracted_samples': []
    }
    
    total_bytes = 0

    for root, dirs, files in os.walk(target_path):
        rel_root = os.path.relpath(root, target_path)
        top_cluster = rel_root.split(os.sep)[0] if rel_root != '.' else '_ROOT_'
        
        if top_cluster not in inventory['clusters']:
            inventory['clusters'][top_cluster] = {
                'files_count': 0,
                'size_mb': 0,
                'extensions': {}
            }
            
        for file in files:
            inventory['total_files'] += 1
            inventory['clusters'][top_cluster]['files_count'] += 1
            
            ext = os.path.splitext(file)[1].lower()
            inventory['extensions'][ext] = inventory['extensions'].get(ext, 0) + 1
            inventory['clusters'][top_cluster]['extensions'][ext] = inventory['clusters'][top_cluster]['extensions'].get(ext, 0) + 1
            
            fpath = os.path.join(root, file)
            try:
                sz = os.path.getsize(fpath)
                total_bytes += sz
                inventory['clusters'][top_cluster]['size_mb'] += sz / (1024 * 1024)
            except Exception:
                sz = 0
                
            # Extraer muestra si es un archivo de texto/guion/documento clave
            if ext in ['.md', '.txt', '.docx', '.doc'] and len(inventory['extracted_samples']) < 250:
                sample = extract_text_sample(fpath, ext)
                if sample and len(sample.strip()) > 30:
                    inventory['extracted_samples'].append({
                        'cluster': top_cluster,
                        'relative_path': os.path.relpath(fpath, target_path),
                        'filename': file,
                        'extension': ext,
                        'size_kb': round(sz / 1024, 2),
                        'sample': sample[:1000]
                    })

    inventory['total_size_mb'] = round(total_bytes / (1024 * 1024), 2)
    for c in inventory['clusters']:
        inventory['clusters'][c]['size_mb'] = round(inventory['clusters'][c]['size_mb'], 2)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)

    print(f"✅ Escaneo completado:")
    print(f"   • Total Archivos: {inventory['total_files']}")
    print(f"   • Volumen Total: {inventory['total_size_mb']} MB")
    print(f"   • Clusters Encontrados: {len(inventory['clusters'])}")
    print(f"   • Muestras de Texto Extraídas: {len(inventory['extracted_samples'])}")
    print(f"   • Reporte guardado en: {output_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escáner Seguro de Solo Lectura para Arqueólogo Creativo")
    parser.add_argument("--path", required=True, help="Ruta de la carpeta copia a auditar")
    parser.add_argument("--output", default="inventory.json", help="Ruta del archivo JSON de salida")
    args = parser.parse_args()
    
    scan_vault(args.path, args.output)
