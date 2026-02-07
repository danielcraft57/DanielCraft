#!/usr/bin/env python3
"""
Système de build pour générer les pages HTML à partir de templates et includes.

Ce script :
1. Lit les fichiers source dans src/
2. Remplace les includes et variables
3. Génère les pages finales dans le dossier racine

Usage:
    python3 build.py              # Build toutes les pages
    python3 build.py --watch      # Mode watch (rebuild automatique)
    python3 build.py index        # Build une page spécifique
"""

import os
import re
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime

# Configuration
BASE_DIR = Path(__file__).parent
SRC_DIR = BASE_DIR / 'src'
INCLUDES_DIR = SRC_DIR / 'includes'
TEMPLATES_DIR = SRC_DIR / 'templates'
PAGES_DIR = SRC_DIR / 'pages'
# Dossier de sortie par défaut : dist/ (peut être modifié via --output)
OUTPUT_DIR = BASE_DIR / 'dist'

# Variables par défaut
DEFAULT_VARS = {
    'page_title': 'Loïc DANIEL - Développeur Full-Stack TypeScript Freelance',
    'page_description': 'Développeur Full-Stack TypeScript freelance avec plus de 7 ans d\'expérience.',
    'page_keywords': 'développeur freelance, full-stack, TypeScript, React, Node.js',
    'page_url': 'https://danielcraft.fr/',
    'og_image': 'https://danielcraft.fr/assets/images/og-image.jpg',
    'og_type': 'website',
    'current_page': '',
    'page_scripts': [],
    'extra_css': None,
    'blog_enabled': False
}


class TemplateEngine:
    """Moteur de template simple avec support includes et variables."""
    
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.includes_cache = {}
    
    def load_include(self, include_path: str) -> str:
        """Charge un fichier include avec cache."""
        if include_path in self.includes_cache:
            return self.includes_cache[include_path]
        
        full_path = self.base_dir / include_path
        if not full_path.exists():
            print(f"[WARN] Include non trouve : {include_path}")
            return f'<!-- Include manquant : {include_path} -->'
        
        content = full_path.read_text(encoding='utf-8')
        self.includes_cache[include_path] = content
        return content
    
    def process_includes(self, content: str, vars_dict: Dict) -> str:
        """Traite les directives {% include %}."""
        pattern = r'\{%\s*include\s+["\']([^"\']+)["\']\s*%\}'
        
        def replace_include(match):
            include_path = match.group(1)
            include_content = self.load_include(include_path)
            # Traite récursivement les includes dans le fichier inclus
            include_content = self.process_includes(include_content, vars_dict)
            # Remplace les variables dans l'include
            include_content = self.replace_variables(include_content, vars_dict)
            return include_content
        
        max_iterations = 20
        for _ in range(max_iterations):
            new_content = re.sub(pattern, replace_include, content)
            if new_content == content:
                break
            content = new_content
        
        return content
    
    def replace_variables(self, content: str, vars_dict: Dict) -> str:
        """Remplace les variables {{variable}}."""
        def replace_var(match):
            var_name = match.group(1)
            value = vars_dict.get(var_name, '')
            
            return str(value) if value is not None else ''
        
        # Remplace {{variable}}
        content = re.sub(r'\{\{(\w+)\}\}', replace_var, content)
        
        # Traite les conditions {% if %}
        content = self.process_conditions(content, vars_dict)
        
        return content
    
    def process_conditions(self, content: str, vars_dict: Dict) -> str:
        """Traite les conditions {% if %} {% else %} {% endif %}."""
        # Pattern pour {% if var == "value" %} ... {% else %} ... {% endif %}
        pattern1 = r'\{%\s*if\s+(\w+)\s*==\s*["\']([^"\']+)["\']\s*%\}(.*?)(?:\{%\s*else\s*%\}(.*?))?\{%\s*endif\s*%\}'
        
        # Pattern pour {% if var %} ... {% else %} ... {% endif %}
        pattern2 = r'\{%\s*if\s+(\w+)\s*%\}(.*?)(?:\{%\s*else\s*%\}(.*?))?\{%\s*endif\s*%\}'
        
        def replace_condition1(match):
            var_name = match.group(1)
            expected_value = match.group(2)
            if_content = match.group(3) or ''
            else_content = match.group(4) or ''
            actual_value = vars_dict.get(var_name, '')
            
            if str(actual_value) == expected_value:
                return if_content
            return else_content
        
        def replace_condition2(match):
            var_name = match.group(1)
            if_content = match.group(2) or ''
            else_content = match.group(3) or ''
            actual_value = vars_dict.get(var_name, '')
            
            # Vérifie si la variable existe et est "truthy"
            if actual_value and actual_value != 'False' and actual_value != 'false':
                if isinstance(actual_value, list) and len(actual_value) > 0:
                    return if_content
                elif not isinstance(actual_value, list):
                    return if_content
            return else_content
        
        max_iterations = 10
        for _ in range(max_iterations):
            new_content = re.sub(pattern1, replace_condition1, content, flags=re.DOTALL)
            new_content = re.sub(pattern2, replace_condition2, new_content, flags=re.DOTALL)
            if new_content == content:
                break
            content = new_content
        
        return content
    
    def render(self, template_path: Path, vars_dict: Dict) -> str:
        """Rend un template avec les variables données."""
        if not template_path.exists():
            raise FileNotFoundError(f"Template non trouvé : {template_path}")
        
        content = template_path.read_text(encoding='utf-8')
        
        # Traite les includes
        content = self.process_includes(content, vars_dict)
        
        # Remplace les variables
        content = self.replace_variables(content, vars_dict)
        
        return content


def load_page_config(page_name: str) -> Dict:
    """Charge la configuration d'une page depuis src/pages/."""
    config_file = PAGES_DIR / f"{page_name}.json"
    
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    return {}


def build_page(page_name: str, template_engine: TemplateEngine):
    """Build une page HTML."""
    # Charge la config de la page
    page_config = load_page_config(page_name)
    
    # Fusionne avec les valeurs par défaut
    vars_dict = DEFAULT_VARS.copy()
    vars_dict.update(page_config)
    vars_dict['current_page'] = page_name
    
    # Génère le contenu des scripts
    scripts = vars_dict.get('page_scripts', [])
    if scripts:
        scripts_content = '\n'.join([
            f'<script src="assets/js/{script}" defer></script>\n<link rel="preload" href="assets/js/{script}" as="script">'
            for script in scripts
        ])
    else:
        scripts_content = '<script src="assets/js/main.js" defer></script>\n<link rel="preload" href="assets/js/main.js" as="script">'
    vars_dict['page_scripts_content'] = scripts_content
    
    # Détermine le template à utiliser
    template_name = page_config.get('template', 'base.html')
    template_path = TEMPLATES_DIR / template_name
    
    if not template_path.exists():
        print(f"[ERREUR] Template non trouve : {template_name}")
        return False
    
    # Charge le contenu de la page
    page_content_file = PAGES_DIR / f"{page_name}.html"
    if page_content_file.exists():
        page_content = page_content_file.read_text(encoding='utf-8')
        vars_dict['page_content'] = page_content
    else:
        print(f"[WARN] Contenu de page non trouve : {page_content_file}")
        vars_dict['page_content'] = f'<!-- Contenu de {page_name} -->'
    
    # Génère le HTML final
    try:
        html_output = template_engine.render(template_path, vars_dict)
        
        # Écrit le fichier de sortie
        output_file = OUTPUT_DIR / f"{page_name}.html"
        output_file.write_text(html_output, encoding='utf-8')
        
        print(f"[OK] {page_name}.html genere")
        return True
    except Exception as e:
        print(f"[ERREUR] Erreur lors du build de {page_name}: {e}")
        return False


def main():
    """Fonction principale."""
    global OUTPUT_DIR
    
    # Parse les arguments
    output_dir_arg = None
    watch_mode = False
    page_name = None
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--output' and i + 1 < len(sys.argv):
            output_dir_arg = sys.argv[i + 1]
            i += 2
        elif arg == '--watch':
            watch_mode = True
            i += 1
        elif not arg.startswith('--'):
            page_name = arg
            i += 1
        else:
            i += 1
    
    # Définit le dossier de sortie
    if output_dir_arg:
        OUTPUT_DIR = BASE_DIR / output_dir_arg
    else:
        OUTPUT_DIR = BASE_DIR / 'dist'
    
    # Crée les dossiers nécessaires
    SRC_DIR.mkdir(exist_ok=True)
    INCLUDES_DIR.mkdir(exist_ok=True)
    TEMPLATES_DIR.mkdir(exist_ok=True)
    PAGES_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Copie les assets dans le dossier de sortie
    assets_src = BASE_DIR / 'assets'
    assets_dst = OUTPUT_DIR / 'assets'
    if assets_src.exists():
        if assets_dst.exists():
            # Suppression plus robuste pour Windows
            try:
                shutil.rmtree(assets_dst)
            except PermissionError:
                # Sur Windows, parfois les fichiers sont verrouillés
                # On essaie de supprimer fichier par fichier
                import stat
                def handle_remove_readonly(func, path, exc):
                    os.chmod(path, stat.S_IWRITE)
                    func(path)
                shutil.rmtree(assets_dst, onerror=handle_remove_readonly)
        shutil.copytree(assets_src, assets_dst)
        print(f"[OK] Assets copies dans {assets_dst}")
    
    # Copie robots.txt et sitemap.xml
    for file in ['robots.txt', 'sitemap.xml']:
        src_file = BASE_DIR / file
        dst_file = OUTPUT_DIR / file
        if src_file.exists():
            shutil.copy2(src_file, dst_file)
            print(f"[OK] {file} copie")

    # Copie du dossier api/ (PHP formulaire contact) vers dist/
    api_src = BASE_DIR / 'api'
    api_dst = OUTPUT_DIR / 'api'
    if api_src.exists():
        api_dst.mkdir(exist_ok=True)
        for f in api_src.iterdir():
            if f.is_file():
                shutil.copy2(f, api_dst / f.name)
        print(f"[OK] api/ copie dans {api_dst}")

    # Crée un favicon.ico à la racine (redirection vers SVG)
    # Note: On crée un fichier vide, nginx redirigera vers le SVG
    favicon_ico = OUTPUT_DIR / 'favicon.ico'
    if not favicon_ico.exists():
        # Crée un fichier SVG minimal comme favicon.ico
        favicon_svg_content = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="#2563eb" rx="20"/><text x="50" y="70" font-family="Arial" font-size="60" font-weight="bold" fill="white" text-anchor="middle">LD</text></svg>'
        favicon_ico.write_text(favicon_svg_content, encoding='utf-8')
        print(f"[OK] favicon.ico cree (redirection vers SVG)")
    
    # Initialise le moteur de template
    template_engine = TemplateEngine(SRC_DIR)
    
    # Si une page spécifique est demandée
    if page_name and not watch_mode:
        if build_page(page_name, template_engine):
            print(f"\n[OK] Build de {page_name} termine dans {OUTPUT_DIR} !")
        else:
            sys.exit(1)
        return
    
    # Build toutes les pages
    print(f"[BUILD] Build de toutes les pages dans {OUTPUT_DIR}...\n")
    
    # Liste des pages à builder
    pages = [
        'index',
        'processus',
        'metz',
        'portfolio',
        'projets',
        'statistiques',
        'mentions-legales',
        'cgv',
        'cgu',
        'politique-confidentialite'
    ]
    
    success_count = 0
    for page in pages:
        if build_page(page, template_engine):
            success_count += 1
    
    print(f"\n[OK] Build termine ! {success_count}/{len(pages)} page(s) generee(s) dans {OUTPUT_DIR}.")
    
    # Mode watch
    if len(sys.argv) > 1 and sys.argv[1] == '--watch':
        print("\n[WATCH] Mode watch active. Appuyez sur Ctrl+C pour arreter.")
        try:
            import time
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            
            class BuildHandler(FileSystemEventHandler):
                def on_modified(self, event):
                    if event.src_path.endswith(('.html', '.json')):
                        print(f"\n📝 Fichier modifié : {event.src_path}")
                        # Détermine quelle page rebuilder
                        for page in pages:
                            if page in event.src_path:
                                build_page(page, template_engine)
                                break
            
            event_handler = BuildHandler()
            observer = Observer()
            observer.schedule(event_handler, str(SRC_DIR), recursive=True)
            observer.start()
            
            while True:
                time.sleep(1)
        except ImportError:
            print("[WARN] Mode watch necessite 'watchdog'. Installez avec: pip install watchdog")
        except KeyboardInterrupt:
            print("\n\n[WATCH] Arret du mode watch.")


if __name__ == '__main__':
    main()

