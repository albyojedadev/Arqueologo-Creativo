import os
import sys
import json
import argparse
import time

sys.stdout.reconfigure(encoding='utf-8')

def scan_vault_metadata_light(target_path, output_json, max_samples=50):
    """
    Escaneo jerárquico y ligero de metadatos (Fase 1):
    Extrae únicamente estructura, extensiones, fechas y metadatos clave para no saturar el Context Window.
    """
    if not os.path.exists(target_path):
        print(f"❌ Error: Path not found / Ruta no encontrada: {target_path}")
        sys.exit(1)

    print(f"🔍 Iniciando escaneo ligero de metadatos en: {target_path}")
    
    inventory = {
        'target_path': target_path,
        'scan_timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'total_files': 0,
        'total_size_mb': 0,
        'extensions': {},
        'clusters': {},
        'key_artifacts_metadata': []
    }
    
    total_bytes = 0

    for root, dirs, files in os.walk(target_path):
        rel_root = os.path.relpath(root, target_path)
        top_cluster = rel_root.split(os.sep)[0] if rel_root != '.' else '_ROOT_'
        
        if top_cluster not in inventory['clusters']:
            inventory['clusters'][top_cluster] = {
                'files_count': 0,
                'size_mb': 0,
                'extensions': {},
                'last_modified': ""
            }
            
        for file in files:
            inventory['total_files'] += 1
            inventory['clusters'][top_cluster]['files_count'] += 1
            
            ext = os.path.splitext(file)[1].lower()
            inventory['extensions'][ext] = inventory['extensions'].get(ext, 0) + 1
            inventory['clusters'][top_cluster]['extensions'][ext] = inventory['clusters'][top_cluster]['extensions'].get(ext, 0) + 1
            
            fpath = os.path.join(root, file)
            try:
                stat = os.stat(fpath)
                sz = stat.st_size
                mtime = time.strftime("%Y-%m-%d", time.localtime(stat.st_mtime))
                total_bytes += sz
                inventory['clusters'][top_cluster]['size_mb'] += sz / (1024 * 1024)
                
                # Actualizar última fecha de modificación del cluster
                if not inventory['clusters'][top_cluster]['last_modified'] or mtime > inventory['clusters'][top_cluster]['last_modified']:
                    inventory['clusters'][top_cluster]['last_modified'] = mtime

                # Registrar metadato ligero de archivos clave sin saturar tokens
                if ext in ['.md', '.txt', '.docx', '.gdd', '.json', '.pdf'] and len(inventory['key_artifacts_metadata']) < max_samples:
                    inventory['key_artifacts_metadata'].append({
                        'cluster': top_cluster,
                        'relative_path': os.path.relpath(fpath, target_path),
                        'filename': file,
                        'extension': ext,
                        'size_kb': round(sz / 1024, 2),
                        'last_modified': mtime
                    })
            except Exception:
                pass

    inventory['total_size_mb'] = round(total_bytes / (1024 * 1024), 2)
    for c in inventory['clusters']:
        inventory['clusters'][c]['size_mb'] = round(inventory['clusters'][c]['size_mb'], 2)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)

    print(f"✅ Escaneo ligero completado con éxito:")
    print(f"   • Total Archivos: {inventory['total_files']}")
    print(f"   • Volumen Total: {inventory['total_size_mb']} MB")
    print(f"   • Clusters Identificados: {len(inventory['clusters'])}")
    print(f"   • Metadatos de Activos Clave: {len(inventory['key_artifacts_metadata'])}")
    print(f"   • Reporte JSON guardado en: {output_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escáner Ligero de Metadatos para Arqueólogo Creativo (V2.5)")
    parser.add_argument("--path", required=True, help="Ruta de la carpeta copia a auditar")
    parser.add_argument("--output", default="inventory_light.json", help="Ruta del archivo JSON de salida")
    parser.add_argument("--samples", type=int, default=50, help="Límite de metadatos de archivos clave")
    args = parser.parse_args()
    
    scan_vault_metadata_light(args.path, args.output, args.samples)
