---
layout: default
title: "🚀 Analyse BIP V5"
---

## 📑 Sommaire
* TOC
{:toc}

---

# 🚀 Analyse BIP V5

Analyseur de fichiers BIP - Interface web Node.js pour analyser les archives ZIP/TAR contenant des fichiers XML.

## 📁 Structure du projet

```
Analyse_BIP_V5/
├── back-bip-analyzer/          # Backend Node.js + Python
│   ├── server.js               # Point d'entrée Express
│   ├── config/                 # Configuration
│   ├── routes/                 # Routes API
│   ├── services/               # Logique métier
│   └── middleware/             # Middlewares
│
├── front-bip-analyzer/          # Frontend JavaScript
│   ├── public/                 # Pages HTML
│   ├── js/                     # Scripts JavaScript
│   └── css/                    # Feuilles de style
│
├── dev-conf-docker/            # Configuration Docker
│   ├── docker-compose.yml
│   ├── config.env.dev
│   ├── config.env.prod
│   └── start.sh
│
├── doc/                        # Documentation
├── uploads/                    # Fichiers uploadés
├── temp/                       # Fichiers temporaires
├── reports/                    # Rapports générés
└── BIP_Files/                  # Fichiers BIP
```

## 🚀 Démarrage rapide

### Avec Docker (recommandé)

```bash
cd dev-conf-docker
./start.sh dev          # Environnement développement
# ou
./start.sh prod         # Environnement production
```.

L'application sera accessible sur **http://localhost:3000**

### Sans Docker

```bash
# Backend
cd back-bip-analyzer
npm install
node server.js

# L'application sera accessible sur http://localhost:3000
```

## 📖 Documentation

- `README Backend` - Configuration et API backend
- `README Frontend` - Structure frontend
- `Guide Docker` - Déploiement Docker complet

## ✨ Fonctionnalités

- ✅ Upload de fichiers ZIP/TAR/TAR.GZ/TGZ
- ✅ Extraction récursive des archives imbriquées
- ✅ Analyse XML personnalisable
- ✅ Génération de rapports Markdown
- ✅ Interface web moderne et responsive
- ✅ Configuration des champs via interface
- ✅ Téléchargement des fichiers XML analysés

## 🛠️ Technologies

- **Backend**: Node.js, Express, Python 3
- **Frontend**: JavaScript Vanilla, CSS3
- **Parsers**: xmldom, adm-zip, tar-fs
- **Docker**: Docker Compose

## 📝 Licence

Propriétaire

## 👥 Contributeurs

Équipe Analyse BIP

