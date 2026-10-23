---
layout: default
title: "Parse Cucumber V2"
---

## 📑 Sommaire
* TOC
{:toc}

---

# Parse Cucumber V2

Application Node.js pour rechercher et modifier des scénarios Cucumber dans JIRA (La Poste).

## Architecture

```
back-cucumber/    # Backend Node.js (API REST, port 3000)
front-cucumber/   # Frontend HTML/JS pur (port 8080)
dev-conf-docker/  # Config Docker, variables d'environnement, script de démarrage
doc/              # Documentation
```

## Démarrage rapide

```bash
# Local (dev)
bash dev-conf-docker/start.sh dev

# Docker Compose
cd dev-conf-docker && docker compose up --build
```

Voir `.github/copilot-instructions.md` pour la documentation complète.  
Voir `doc/README_AUTH.md` pour la récupération du Personal Access Token JIRA.

