import os

replacements = [
    ("ShrutiBuilder", "ShrutiBuilder"),
    ("ShrutiBuilder", "ShrutiBuilder"),
    ("SHRUTIBUILDER", "SHRUTIBUILDER")
]

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content
        for old, new in replacements:
            new_content = new_content.replace(old, new)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced in {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")

for root, d, files in os.walk(r'c:\Users\HP\PPT GENRATOR AGENT\ShrutiBuilder-ppt-generator'):
    if 'venv' in root or '.git' in root or 'output' in root or '__pycache__' in root:
        continue
    for f in files:
        if f.endswith('.py') or f.endswith('.md'):
            replace_in_file(os.path.join(root, f))
