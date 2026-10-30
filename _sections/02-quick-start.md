---
title: "Quick Start"
icon: "🚀"
order: 2
---
## Démarrer en 5 minutes

---

## Prérequis (à vérifier une seule fois)

| # | Prérequis | Vérification rapide |
|---|---|---|
| 1 | **Node.js ≥ 18** | `node --version` dans un terminal |
| 2 | **VS Code ≥ 1.90** | Menu Aide → À propos |
| 3 | **GitHub Copilot actif** | Icône Copilot visible en bas de VS Code |
| 4 | **VPN La Poste** *(pour JIRA uniquement)* | Requis hors site pour publier dans JIRA |

---

## Étape 1 — Ouvrir MAX dans VS Code

```
Fichier → Ouvrir le dossier… → sélectionner MAX_PI_V2
```

Attendez que VS Code charge le workspace et active les extensions.

---

## Étape 2 — Installer le proxy LLM *(une seule fois)*

Le proxy fait le lien entre MAX et GitHub Copilot.

```
Ctrl+Shift+P → Tasks: Run Task → Installer MAX Copilot Proxy
```

Redémarrez VS Code quand le message `✅ Extension MAX Copilot Proxy installée` s'affiche.

> **Vérification :** `Ctrl+Shift+P` → `MAX: Statut du proxy Copilot` → doit indiquer "actif sur le port 3099"

---

## Étape 3 — Démarrer le serveur MAX

Ouvrez un terminal dans VS Code (`Ctrl+ù`) et lancez :

```bash
cd back-max
node server.js
```

Le terminal doit afficher :
```
✅ Configuration chargée avec succès
🥒 Parse Cucumber V2 démarré sur le port interne 3002
🚀 MAX démarré sur http://localhost:8082
```

---

## Étape 4 — Se connecter à MAX

Ouvrez votre navigateur : **http://localhost:8082**

### Mode développement (sans VPN)

Laissez `DEV_MODE=true` dans `dev-conf-docker/config.env` (valeur par défaut).  
Saisissez n'importe quelle valeur dans le champ PAT → MAX démarre en mode "Dev User".

### Mode production (avec VPN La Poste)

1. Dans `dev-conf-docker/config.env`, passez `DEV_MODE=false`
2. Générez votre PAT JIRA : `jira.net.extra.laposte.fr` → Profil → Security → Personal Access Tokens
3. Saisissez votre PAT dans l'écran de connexion MAX

---

## Étape 5 — Premier test : analyser une SPECS et générer des US

1. Dans le menu latéral, cliquez sur **📋 Analyseur de SPECS et Génération d'US**
2. Cliquez sur **📄 Charger une exigence .md** et sélectionnez un fichier de spécifications
3. Tapez dans le chat : `Analyse les SPECS et génère les User Stories`
4. MAX analyse le document, extrait les exigences EF-001… et génère les US + CA
5. Cliquez sur **⬇️ Télécharger .md** pour exporter le résultat

---

## Étape 6 — Générer des tests Gherkin et publier dans JIRA

1. Dans le menu, cliquez sur **🥒 Génération de Cas de Tests Fonctionnels en Gherkin**
2. Chargez vos US générées à l'étape 5 (**📄 Charger une exigence .md**)  
   — ou chargez directement un ticket JIRA (**🎫 Charger une exigence JIRA**)
3. Tapez : `Génère les scénarios de tests Gherkin`
4. MAX génère les Feature files BDD complets
5. Cliquez sur **📤 Publier dans JIRA**, saisissez la clé projet (ex : `PROJ`) et confirmez
6. MAX crée les tickets Xray, les décrit et les étiquette `Généré_par_IA_MAX`

> 💡 Si une publication est erronée, cliquez sur **🗑️ Annuler les Tickets** pour supprimer tous les tickets créés.

---

## Récapitulatif des commandes

| Action | Commande |
|---|---|
| Démarrer le serveur | `cd back-max && node server.js` |
| Arrêter le serveur | `Ctrl+C` dans le terminal |
| Redémarrer (Windows) | `taskkill /f /im node.exe` puis `node server.js` |
| Accéder à MAX | `http://localhost:8082` |
| Vérifier le proxy LLM | `Ctrl+Shift+P` → `MAX: Statut du proxy Copilot` |

---

## Configuration essentielle (`dev-conf-docker/config.env`)

```dotenv
PORT=8082                              # Port du serveur MAX
DEV_MODE=true                          # true = pas de VPN requis, false = JIRA réel
LLM_BASE_URL=http://127.0.0.1:3099/v1  # Proxy Copilot (ne pas modifier)
GITHUB_TOKEN=copilot-proxy             # Ne pas modifier
GITHUB_MODEL=gpt-5.4                   # Modèle LLM (gpt-4o, claude-sonnet-4-5…)
# JIRA_URL=https://jira.net.extra.laposte.fr/jira  # Décommenter si URL différente
```

---

## Résolution des problèmes courants

| Symptôme | Cause probable | Solution |
|---|---|---|
| Page blanche sur http://localhost:8082 | Serveur non démarré | `cd back-max && node server.js` |
| `GITHUB_TOKEN non configuré` | Proxy LLM inactif | Réinstaller MAX Copilot Proxy (Étape 2) |
| Connexion JIRA impossible | VPN non connecté ou `DEV_MODE=false` | Activer VPN ou passer `DEV_MODE=true` |
| Port 8082 déjà utilisé | Ancien processus node en mémoire | `taskkill /f /im node.exe` puis relancer |
| Étiquettes parasites sur tickets JIRA | Normal avant V6 | Corrigé en V6 : seul `Généré_par_IA_MAX` est appliqué |
| Bouton "Annuler les Tickets" grisé | État `disabled` persistant d'une session précédente | Corrigé en V6 : le bouton se réactive automatiquement |

---

## Pour aller plus loin

| Document | Contenu |
|---|---|
| [Présentation_MAX_V6.md](Présentation_MAX_V6.md) | Valeur ajoutée, agents IA, fonctionnalités détaillées |
| [ARCHITECTURE_MAX_V6.md](ARCHITECTURE_MAX_V6.md) | Architecture technique complète (composants, API, ports) |
| [modop_Install_MAX_V6.md](modop_Install_MAX_V6.md) | Guide d'installation complet (proxy, Docker, DiversIT) |
