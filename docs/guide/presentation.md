---
layout: default
title: "MAX — Présentation Générale"
---

## 📑 Sommaire
* TOC
{:toc}

---

# MAX — Présentation Générale
## Maintenance Augmentée et Accélérée des Tests · La Poste

---

## Qu'est-ce que MAX ?

**MAX** (Maintenance Augmentée et Accélérée des Tests) est une plateforme d'IA intégrée à VS Code et au navigateur web, conçue pour automatiser et accélérer la chaîne de production des tests fonctionnels BDD au sein des équipes agiles de La Poste.

MAX couvre l'intégralité du pipeline qualité, de la lecture du cahier des charges jusqu'à la publication automatique des tickets de tests dans JIRA/Xray :

```
  Cahier des charges      User Stories          Tests Gherkin         JIRA / Xray
  (SPECS .md / .docx)  →  + Critères d'acc.  →  (Feature files)   →  (tickets Test)
         │                      │                      │                    │
    Agent Analyseur        Agent Générateur       Agent Gherkin        Publication
    de SPECS               US & CA                & JIRA               automatique
```

MAX n'est **pas** un simple générateur de texte. C'est un assistant métier expert **ISTQB** qui connaît les règles de La Poste, les conventions Xray et les bonnes pratiques BDD.

---

## Valeur ajoutée pour les acteurs agiles

### Pour le **Product Owner**
- Transforme instantanément un cahier des charges en User Stories structurées et priorisées
- Extrait automatiquement les acteurs, exigences fonctionnelles (EF-001…) et les ambiguïtés
- Produit des US au format standard : *"En tant que [rôle], je veux [action], afin de [bénéfice]"*
- Génère les critères d'acceptation Given/When/Then attachés à chaque US
- **Gain estimé : 60 à 80 % du temps de rédaction des US**

### Pour le **Test Manager**
- Pipeline traçable bout-en-bout : chaque scénario est lié à son US source et à son exigence d'origine
- Couverture ISTQB garantie : nominal, alternatif, cas d'erreur, valeurs limites
- Export .docx pour revue et archivage
- Labels JIRA automatiques (`Généré_par_IA_MAX`) pour filtrer les tests générés par IA
- Chaque ticket Test contient dans sa description l'identifiant CA et la fonctionnalité couverte

### Pour le **Testeur / QA Engineer**
- Génère en quelques secondes des scénarios Gherkin complets et exploitables dans Cucumber
- Publie directement dans JIRA en tant que tickets Xray (type Test), sans manipulation manuelle
- Permet d'éditer et de corriger des scénarios Gherkin existants via la vue Cucumber
- Charge n'importe quel ticket JIRA existant comme source d'exigence
- **Gain estimé : 70 % du temps de rédaction des tests fonctionnels**

### Pour le **Développeur / Tech Lead**
- Les Feature files générés sont directement exécutables avec Cucumber
- Format `# language: fr` normalisé, compatible Xray Server v1 et v2
- Possibilité d'annuler une publication JIRA entière d'un clic (bouton "Annuler les Tickets")
- Intégration transparente dans VS Code via Copilot Chat — aucun outil tiers à installer

---

## Les 3 agents IA de MAX

MAX s'appuie sur trois agents GitHub Copilot spécialisés, activables dans VS Code via le panneau Copilot Chat ou via l'interface web. Chaque agent est un expert métier précis.

---

### Agent 1 — MAX Analyseur de SPECS

> *"Je lis votre cahier des charges et j'en extrais une structure exploitable"*

**Modèle :** Claude Sonnet 4.5 · **Outils :** lecture fichiers, recherche

**Ce qu'il fait :**

1. Lit le document SPECS fourni (fichier `.md`, `.docx` ou contenu collé directement)
2. Identifie tous les **acteurs et rôles métier** impliqués dans le système
3. Extrait et numérote les **exigences fonctionnelles** (`EF-001`, `EF-002`…) et **non-fonctionnelles** (`ENF-001`…)
4. Pour chaque exigence : décrit la précondition, l'acteur, le résultat attendu et les règles métier
5. Signale explicitement les **zones d'ambiguïté** et le **périmètre exclu** plutôt que d'inventer
6. **Ne génère pas** de User Stories — son rôle est de structurer, pas d'interpréter

**Format de sortie :**
```
# Analyse SPECS — [Titre du document]
## Acteurs identifiés
## Exigences fonctionnelles
  ### EF-001 — [Titre]
  - Description, Acteur, Préconditions, Résultat attendu, Règles métier
## Exigences non-fonctionnelles
## Zones d'ambiguïté
## Périmètre exclu
```

**Comment l'activer :**
- Dans VS Code Copilot Chat : `@MAX — Analyseur de SPECS doc/mon-cahier.md`
- Dans l'interface web MAX : menu *Analyseur de SPECS* → bouton *Charger une exigence*

---

### Agent 2 — MAX Générateur US & CA

> *"Je transforme vos exigences en User Stories ISTQB avec leurs critères d'acceptation"*

**Modèle :** Claude Sonnet 4.5 · **Outils :** lecture fichiers, recherche

**Ce qu'il fait :**

1. Lit l'analyse produite par l'Agent 1 (ou des exigences brutes directement)
2. Crée **une User Story par exigence fonctionnelle** principale (décompose si complexe)
3. Rédige les **critères d'acceptation en Gherkin condensé** (Given/When/Then)
4. Applique systématiquement les techniques **ISTQB** :
   - Partitionnement d'équivalence
   - Analyse des valeurs limites
   - Tables de décision
5. Pour chaque US, produit au minimum : un **cas nominal** (CA-001), un **cas alternatif** (CA-002) et un **cas d'erreur** (CA-003)
6. Indique la priorité (Haute / Moyenne / Basse) et la traçabilité vers l'exigence source

**Format de sortie :**
```
## US-001 — [Titre court et parlant]
En tant que [rôle], Je veux [action], Afin de [bénéfice].
Priorité : Haute · Exigence source : EF-001

### Critères d'acceptation
CA-001 — [Cas nominal]
  Étant donné / Quand / Alors

CA-002 — [Cas alternatif]
CA-003 — [Cas d'erreur / valeur limite]
```

**Comment l'activer :**
- Dans VS Code Copilot Chat : `@MAX — Générateur US & CA` (après une analyse SPECS)
- Dans l'interface web MAX : menu *Analyseur de SPECS* → bouton *Générer les US*

---

### Agent 3 — MAX Générateur Gherkin & JIRA

> *"Je rédige vos Feature files BDD et je les publie dans JIRA en tant que tickets Xray"*

**Modèle :** Claude Sonnet 4.5 · **Outils :** lecture, recherche + **6 outils MCP Atlassian**

**Ce qu'il fait :**

1. Lit les User Stories et CA fournis (ou charge directement un ticket JIRA via sa clé)
2. Génère des **scénarios Gherkin complets** par US, au format `# language: fr`
3. Structure chaque Feature file avec : tags (`@fonctionnel @regression @xray`), contexte partagé, scénarios nominaux/alternatifs/erreur, plans de scénarios avec exemples pour les valeurs limites
4. Propose les scénarios à l'utilisateur pour **validation avant toute publication**
5. Publie dans JIRA sous forme de **tickets de type Test (Xray)** sur confirmation explicite
6. Via l'interface web : met à jour chaque ticket avec sa description structurée et son étiquette

**Format Gherkin produit :**
```gherkin
# language: fr
@fonctionnel @regression @xray
Feature: [Titre de la fonctionnalité — reprend le titre de la US]

  En tant que [rôle]
  Je veux [action]
  Afin de [bénéfice]

  Contexte:
    Étant donné [précondition commune]

  @smoke
  Scénario: [Titre du cas nominal — CA-001]
    Étant donné [contexte précis]
    Quand [action de l'acteur]
    Alors [résultat observable et vérifiable]

  Plan du scénario: [Valeurs limites — CA-004]
    Étant donné [contexte avec <paramètre>]
    Quand [action avec <valeur>]
    Alors [résultat <attendu>]
    Exemples:
      | paramètre | valeur | attendu |
```

**Outils MCP Atlassian utilisés (Copilot Chat uniquement) :**
| Outil | Usage |
|---|---|
| `getJiraIssue` | Charger la US source depuis JIRA |
| `createJiraIssue` | Créer un ticket Test avec le Gherkin |
| `editJiraIssue` | Mettre à jour un ticket existant |
| `addCommentToJiraIssue` | Ajouter le Gherkin en commentaire |
| `getVisibleJiraProjects` | Lister les projets disponibles |
| `fetch` | Appels REST JIRA génériques |

**Comment l'activer :**
- Dans VS Code Copilot Chat : `@MAX — Générateur Gherkin & JIRA US-001 — Titre`
- Dans l'interface web MAX : menu *Génération de Tests* → chat + bouton *Publier dans JIRA*

---

## Fonctionnalités de l'interface web

L'interface web MAX (`http://localhost:8082`) est accessible depuis n'importe quel navigateur après authentification avec le PAT JIRA.

### Menu — Analyseur de SPECS et Génération d'US

| Fonctionnalité | Description |
|---|---|
| 📄 **Charger une exigence .md** | Importe un fichier Markdown comme source SPECS |
| 📎 **Charger une exigence .docx** | Parse un fichier Word et extrait le texte |
| 🎫 **Charger depuis JIRA** | Charge la description d'un ticket JIRA (clé PROJ-123) |
| 📋 **Analyser les SPECS** | Lance l'Agent 1 — extrait EF, acteurs, ambiguïtés |
| 📋 **Générer les US** | Lance l'Agent 2 — produit les US + CA au format Gherkin condensé |
| ⬇️ **Télécharger .md** | Exporte le résultat en fichier Markdown |
| ⬇️ **Télécharger .docx** | Exporte le résultat en fichier Word |
| 🎫 **Formater en JIRA** | Prépare les US pour publication dans JIRA |

---

### Menu — Génération de Cas de Tests Fonctionnels en Gherkin

| Fonctionnalité | Description |
|---|---|
| 🎫 **Charger une exigence JIRA** | Charge la description + résumé d'un ticket JIRA |
| 📄 **Charger une exigence .md** | Importe un fichier Markdown (US + CA) |
| 📎 **Charger une exigence .docx** | Parse un fichier Word |
| 💬 **Chat IA** | Génération temps-réel via stream SSE, conversation continue |
| ⬇️ **Télécharger les Tests .md** | Exporte les scénarios Gherkin en Markdown |
| ⬇️ **Télécharger les Tests .docx** | Exporte les scénarios Gherkin en Word |
| 📤 **Publier dans JIRA** | Import Xray + description structurée + étiquette `Généré_par_IA_MAX` |
| 🗑️ **Annuler les Tickets** | Supprime les tickets créés lors de la dernière publication |

**Détail de la publication JIRA :**
- **Étape 1/2** : Reformatage XRAY via LLM (sauvegarde `tests.md`)
- **Étape 2/2** : Import multipart vers Xray (`/rest/raven/1.0/import/feature`)
- Chaque ticket créé reçoit automatiquement :
  - **Description** : `"Test du CA-001 - [titre du scénario]"` + `"Ce test couvre la Fonctionnalité US-001 - [titre US]"`
  - **Étiquette** : `Généré_par_IA_MAX` (remplace toutes les étiquettes Xray générées automatiquement)

---

### Menu — Modifier un scénario Gherkin d'un Ticket Test

| Fonctionnalité | Description |
|---|---|
| 🔍 **Rechercher** | Trouve des tickets Test Xray existants dans JIRA |
| ✏️ **Éditer** | Modifie le contenu Gherkin d'un scénario existant |
| 💾 **Mettre à jour** | Publie les modifications dans JIRA |

Cette fonctionnalité est assurée par le module **Parse Cucumber V2** (service interne), qui dialogue directement avec l'API JIRA pour lire et écrire les scénarios Gherkin des tickets Test existants.

---

## Pipeline MAX bout-en-bout

```
┌──────────────────────────────────────────────────────────────────────┐
│  Document source : cahier des charges, .md, .docx ou ticket JIRA     │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │   AGENT 1       │  ← Analyseur de SPECS
                    │                 │
                    │  EF-001 à EF-n  │
                    │  Acteurs        │
                    │  Ambiguïtés     │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   AGENT 2       │  ← Générateur US & CA
                    │                 │
                    │  US-001 à US-n  │
                    │  CA-001 nominal │
                    │  CA-002 altern. │
                    │  CA-003 erreur  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   AGENT 3       │  ← Générateur Gherkin & JIRA
                    │                 │
                    │  Feature files  │
                    │  # language: fr │
                    │  @xray          │
                    │  Scénarios BDD  │
                    └────────┬────────┘
                             │
               ┌─────────────▼──────────────┐
               │  JIRA / Xray La Poste       │
               │                            │
               │  Tickets de type "Test"     │
               │  Description structurée     │
               │  Label Généré_par_IA_MAX    │
               │  Prêts pour exécution       │
               └────────────────────────────┘
```

---

## Prérequis et démarrage rapide

| Prérequis | Détail |
|---|---|
| **Node.js ≥ 18** | Exécution du serveur back-max |
| **VS Code ≥ 1.90** | IDE hôte |
| **GitHub Copilot** | Abonnement actif (fournit le LLM) |
| **VPN La Poste** | Requis pour accéder à JIRA (hors site) |
| **PAT JIRA** | Token personnel généré sur `jira.net.extra.laposte.fr` |

**Démarrage :**
```bash
# 1. Installer l'extension proxy LLM (une seule fois)
#    VS Code : Ctrl+Shift+P → "Tasks: Run Task" → "Installer MAX Copilot Proxy"

# 2. Démarrer le serveur
cd back-max
node server.js

# 3. Ouvrir MAX dans le navigateur
# http://localhost:8082
# Saisir votre PAT JIRA pour vous connecter
```

---

## Résumé des gains attendus

| Tâche | Temps sans MAX | Temps avec MAX | Gain |
|---|---|---|---|
| Analyse d'un cahier des charges | 2–4 h | 15–30 min | **~80 %** |
| Rédaction des User Stories | 3–6 h | 20–40 min | **~85 %** |
| Rédaction des scénarios Gherkin | 4–8 h | 15–30 min | **~90 %** |
| Publication dans JIRA | 1–2 h | 2–5 min | **~95 %** |
| **Pipeline complet SPECS → JIRA** | **10–20 h** | **1–2 h** | **~90 %** |

> Les gains varient selon la complexité du projet et l'expérience de l'utilisateur.
> MAX produit une base solide ; la relecture humaine et l'ajustement métier restent indispensables.

