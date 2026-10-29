import os
import shutil

prod_dir = r"C:\JC\VSCODE\Prod_Releases"
doc_repo = r"C:\JC\VSCODE\Prod_Releases\documentation-max"
docs_dir = os.path.join(doc_repo, "docs")

# Mapping des sources d'origine vers la doc
files_to_copy = [
    (os.path.join(prod_dir, "max-git-v6", "doc", "Quick_Start.md"), os.path.join(docs_dir, "guide", "quick-start.md")),
    (os.path.join(prod_dir, "max-git-v6", "doc", "Présentation_MAX_V6.md"), os.path.join(docs_dir, "guide", "presentation.md")),
    (os.path.join(prod_dir, "max-git-v6", "doc", "modop_Install_MAX_V6 - V2.md"), os.path.join(docs_dir, "guide", "installation.md")),
    (os.path.join(prod_dir, "max-git-v6", "doc", "Notes-de-Version_V6.md"), os.path.join(docs_dir, "guide", "release-notes.md")),
    (os.path.join(prod_dir, "max-git-v6", "doc", "ARCHITECTURE_MAX_V6.md"), os.path.join(docs_dir, "architecture", "architecture.md")),
]

for src, dst in files_to_copy:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        # Lire en détectant l'encodage
        content = None
        for enc in ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252']:
            try:
                with open(src, 'r', encoding=enc) as f:
                    content = f.read()
                break
            except Exception:
                continue
        
        # Nettoyages des liens
        content = content.replace("[Présentation_MAX_V6.md](Présentation_MAX_V6.md)", "[Présentation MAX V6](presentation.html)")
        content = content.replace("[ARCHITECTURE_MAX_V6.md](ARCHITECTURE_MAX_V6.md)", "[Architecture MAX V6](../architecture/architecture.html)")
        content = content.replace("[modop_Install_MAX_V6.md](modop_Install_MAX_V6.md)", "[Guide d'installation](installation.html)")
        content = content.replace("[README Backend](back-bip-analyzer/README.md)", "`README Backend`")
        content = content.replace("[README Frontend](front-bip-analyzer/README.md)", "`README Frontend`")
        content = content.replace("[Guide Docker](doc/README-DOCKER.md)", "`Guide Docker`")
        content = content.replace("[`.github/copilot-instructions.md`](.github/copilot-instructions.md)", "`.github/copilot-instructions.md`")
        content = content.replace("[`doc/README_AUTH.md`](doc/README_AUTH.md)", "`doc/README_AUTH.md`")

        title = os.path.basename(dst).replace('.md', '').capitalize()
        for line in content.splitlines():
            if line.startswith('# '):
                title = line.replace('# ', '').replace('"', '').strip()
                break

        full_md = f'---\nlayout: default\ntitle: "{title}"\n---\n\n## 📑 Sommaire\n* TOC\n{{:toc}}\n\n---\n\n{content}\n'
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(full_md)
        print(f"Copied & processed: {os.path.basename(dst)} (Title: {title})")

print("All files processed successfully.")
