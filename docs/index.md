---
layout: default
title: "Documentation MAX V6"
---

## 📑 Sommaire
* TOC
{:toc}

---

# Documentation MAX V6

Bienvenue sur la documentation officielle du projet **MAX V6** (Module d'Assistance eXpert).

MAX est une plateforme d'IA gÃ©nÃ©rative conÃ§ue pour accÃ©lÃ©rer et fiabiliser la chaÃ®ne de delivery agile : de l'analyse des spÃ©cifications fonctionnelles jusqu'Ã  la publication des scÃ©narios de test dans JIRA / Xray.

---

## ðŸš€ AccÃ¨s rapide

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **[DÃ©marrer en 5 minutes](guide/quick-start.md)**

    ---

    PrÃ©requis, lancement du serveur, connexion et premiers tests en mode local ou connectÃ©.

-   :material-presentation:{ .lg .middle } **[PrÃ©sentation & FonctionnalitÃ©s](guide/presentation.md)**

    ---

    DÃ©couvrez les agents IA, les cas d'usage et la valeur ajoutÃ©e pour les Ã©quipes produit et QA.

-   :material-server-network:{ .lg .middle } **[Architecture technique](architecture/architecture.md)**

    ---

    SchÃ©mas d'architecture, microservices, ports rÃ©seau, flux de donnÃ©es et intÃ©grations.

-   :material-cog:{ .lg .middle } **[Installation & DÃ©ploiement](guide/installation.md)**

    ---

    Guide complet pas-Ã -pas : proxy VS Code Copilot, Docker Compose et environnements d'hÃ©bergement.

</div>

---

## ðŸŽ¯ FonctionnalitÃ©s clÃ©s de MAX V6

```mermaid
flowchart LR
    A[ðŸ“„ Document SPECS] --> B[ðŸ“‹ Analyseur SPECS & US]
    B --> C[User Stories & CA]
    C --> D[ðŸ¥’ GÃ©nÃ©rateur Gherkin]
    D --> E[ScÃ©narios BDD]
    E --> F[ðŸŽ« Publication JIRA / Xray]
```

1. **ðŸ“‹ Analyseur de SpÃ©cifications et GÃ©nÃ©rateur d'US** : Extraction automatique des exigences (`EF-xxx`), gÃ©nÃ©ration des User Stories avec critÃ¨res d'acceptation dÃ©taillÃ©s.
2. **ðŸ¥’ GÃ©nÃ©rateur de tests Gherkin BDD** : CrÃ©ation automatique de fichiers Features et scÃ©narios de tests BDD conformes ISTQB.
3. **ðŸŽ« IntÃ©gration JIRA / Xray** : Import direct depuis un ticket JIRA et publication automatisÃ©e des tests crÃ©Ã©s avec traÃ§abilitÃ©.
4. **ðŸ”’ Respect de la confidentialitÃ© des donnÃ©es** : Fonctionnement via GitHub Copilot Proxy ou modÃ¨les d'entreprise sans fuite de donnÃ©es.

---

## ðŸ“¦ Modules et composants

Explorez la documentation dÃ©taillÃ©e des composants du projet :

- **[Backend (back-max)](modules/backend.md)** : API REST, orchestration des agents, proxies d'appels.
- **[Frontend (front-max)](modules/frontend.md)** : Interface utilisateur unifiÃ©e, gestion de sessions.

