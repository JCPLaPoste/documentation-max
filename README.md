# 📚 Documentation MAX V6

Site officiel : **[https://jcplaposte.github.io/documentation-max/](https://jcplaposte.github.io/documentation-max/)**

Ce dépôt héberge et compile la documentation technique et fonctionnelle du projet **MAX V6** (Module d'Assistance eXpert).

---

## 🏗️ Structure de la documentation

Le site est généré via **MkDocs Material** avec :
- 📑 Navigation arborescente à gauche
- 🔍 Recherche plein texte instantanée
- 📌 Table des matières (TOC) dynamique par page à droite
- 🌓 Bascule mode clair / mode sombre
- 📊 Rendu des diagrammes Mermaid

### Organisation des pages (`docs/`) :
- `index.md` : Accueil et présentation du projet
- `guide/` :
  - `quick-start.md` : Démarrage rapide en 5 minutes
  - `presentation.md` : Présentation détaillée & valeur ajoutée
  - `installation.md` : Mode opératoire d'installation complet
  - `release-notes.md` : Notes de version V6
- `architecture/` :
  - `architecture.md` : Architecture technique, composants, ports et flux
- `modules/` :
  - `backend.md` : Serveur back-max & microservices
  - `frontend.md` : IHM front-max

---

## 🛠️ Commandes utiles

### Prévisualiser en local :
```bash
python -m pip install mkdocs-material
mkdocs serve
```
Puis ouvrir `http://127.0.0.1:8000` dans votre navigateur.

### Resynchroniser les fichiers `.md` depuis les dépôts locaux :
```powershell
powershell ./scripts/sync-docs.ps1
```

### Déploiement :
Chaque commit et push sur la branche `main` déclenche le workflow GitHub Actions `.github/workflows/deploy.yml` qui met à jour automatiquement le site GitHub Pages :
[https://jcplaposte.github.io/documentation-max/](https://jcplaposte.github.io/documentation-max/)
