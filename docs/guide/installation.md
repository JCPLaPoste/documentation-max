---
layout: default
title: "Mode Opératoire — Installation et utilisation de MAX sous VS Code"
---

## 📑 Sommaire
* TOC
{:toc}

---

# Mode Opératoire — Installation et utilisation de MAX sous VS Code
## Testeurs — Guide pas à pas

> **Produit :** MAX V6 — Maintenance Augmentée et Accélérée des Tests
> **Public :** Testeurs, Test Managers, Product Owners
> **Prérequis :** Windows + VS Code + GitHub Copilot (abonnement actif)

---

## Prérequis à vérifier avant de commencer

| Prérequis | Vérification |
|-----------|-------------|
| **Node.js ≥ 18** | `node --version` dans un terminal | extension de VSCODE : Node Modules
| **VS Code** | Version ≥ 1.90 |
| **GitHub Copilot** | Abonnement actif + connecté dans VS Code | vérifier dans comptes prenom.nom_bscc (GitHub) connecté
| **Accès réseau JIRA** | VPN La Poste actif (si hors site) |
| **Proxy réseau** (Utilisateurs Externes DiversIT) | Configurer le proxy avant d'accéder à MAX — voir section dédiée ci-dessous |

> ⚠️ **Utilisateurs Externes (DiversIT)** : votre réseau nécessite une configuration de proxy spécifique pour accéder à MAX. Consultez la section **[Configuration du Proxy pour Utilisateurs Externes](#configuration-du-proxy-pour-utilisateurs-externes-diversit)** avant de continuer.

---
## INSTALLATION DE NODE.JS SUR LE PC

** Dans un terminal powershell **

> (il faut les droits admin) Pour les personnes qui ont des droits administrateurs sur leur PC

```Terminal powershell : Exécuter ces 2 commandes 

winget install OpenJS.NodeJS.LTS --force

winget upgrade OpenJS.NodeJS

```

** Solution de contournement pour les personnes qui ne disposent pas des droits admin sur leur PC **

> Aller dans https://nodejs.org/en/download
 
> Prendre la version "Standalone"
 
> Dézipper le fichier obtenu
> télécharger dans un dossier "C:\Tools\nodejs"
> Ensuite, lancer avec :
```Terminal powershell : Exécuter ces 3 commandes 	
	cd .\back-max\
	$env:PATH="C:\Tools\nodejs\node-v24.21.0-win-x64;$env:PATH"
	node server.js
```
```Installation des modules nodes (toujours dans \back-max\)
   npm.cmd install --verbose
```

## Installation de VSCODE

(depuis le navigateur pas besoin d'être admin) : https://code.visualstudio.com/download?_exp_download=fb315fc982

## Associer Github Copilot à VSCODE
Se connecter à https://github.com/settings/copilot/features
> Aller dans Settings (ou menu de Gauche Copilot>Features)
> Dans Getting Started / Install copilot in your editor, Choisir "Visual Studio Code"

## Mettre Visual Studio Code en français, 

installer l'extension officielle French Language Pack for Visual Studio Code depuis le marché Visual Studio Marketplace.
Étapes pour changer la langue
> 1. Ouvrir Visual Studio Code.
> 2. Cliquer sur l'icône des Extensions dans la barre latérale gauche (ou appuyez sur Ctrl + Maj + X / Cmd + Maj + X).
> 3. Taper "French" dans la barre de recherche.
> 4. Sélectionner l'extension French Language Pack for Visual Studio Code publiée par Microsoft et cliquez sur Install.
> 5. Une notification apparaît en bas à droite proposant de redémarrer l'application ;
> 6. Cliquer sur Change Language et Redémarrer VSCODE.

Si la notification ne s'affiche pas ou si l'interface reste en anglais :
> Ouvrir la palette de commandes avec le raccourci Ctrl + Maj + P (Windows/Linux) ou Cmd + Maj + P (Mac).
> Taper "Configure Display Language" (ou Configurer la langue d'affichage) et valider avec Entrée.
> Choisir français dans la liste déroulante.
> Redémarrer VS CODE pour appliquer les modifications.


## Configuration du Proxy pour Utilisateurs Externes (DiversIT)

> ⚠️ **Cette section s'adresse uniquement aux prestataires et utilisateurs externes (DiversIT).**
> Les collaborateurs La Poste sur le réseau interne peuvent passer directement à l'[Étape 1](#étape-1--ouvrir-le-projet-dans-vs-code).

La mention suivante s'affiche sur la page de connexion MAX pour rappel :

> *"Utilisateurs Externes (DiversIT), veuillez configurer votre Proxy pour accèder à MAX"*

### Pourquoi un proxy est nécessaire ?

Les utilisateurs externes (DiversIT) accèdent aux services La Poste (JIRA, API MAX) via un proxy réseau fourni par leur responsable technique. Sans cette configuration, les appels réseau échoueront.

### Configuration du proxy dans VS Code

1. Ouvrez les paramètres VS Code : `Ctrl+Shift+P` → `Preferences: Open Settings (JSON)`
2. Ajoutez ou vérifiez les entrées suivantes :

```json
{
  "http.proxy": "http://<ADRESSE_PROXY>:<PORT>",
  "http.proxyStrictSSL": false,
  "http.proxyAuthorization": null
}
```

> Remplacez `<ADRESSE_PROXY>` et `<PORT>` par les valeurs fournies par votre responsable technique DiversIT.

### Configuration du proxy dans Node.js (serveur MAX)

Si le serveur MAX doit passer par le proxy pour joindre JIRA et le LLM, ajoutez les variables d'environnement dans `dev-conf-docker/config.env` :

```dotenv
# Proxy pour utilisateurs externes (DiversIT)
HTTP_PROXY=http://<ADRESSE_PROXY>:<PORT>
HTTPS_PROXY=http://<ADRESSE_PROXY>:<PORT>
NO_PROXY=localhost,127.0.0.1
```

### Vérification

Une fois le proxy configuré, vérifiez que vous accédez bien à :
- `http://localhost:8082` — serveur MAX local (ne passe pas par le proxy)
- `https://jira.net.extra.laposte.fr/jira` — JIRA La Poste (doit passer par le proxy)

---

## Étape 1 — Ouvrir le projet dans VS Code

1. Lancez **VS Code**
2. Faites `Fichier > Ouvrir le dossier…` et sélectionnez le dossier `MAX_V6`
3. VS Code charge le workspace — attendez que les extensions s'activent

---

## Étape 2 — Installer l'extension proxy LLM (une seule fois)

L'extension **MAX Copilot Proxy** fait le pont entre le serveur MAX et GitHub Copilot.
Elle doit être installée **une seule fois** sur votre VS Code.

### Via la tâche VS Code (recommandé)

1. Ouvrez la palette de commandes : `Ctrl+Shift+P`
2. Tapez : `Tasks: Run Task`
3. Sélectionnez : **Installer MAX Copilot Proxy**
4. Attendez le message : `✅ Extension MAX Copilot Proxy installée.`
5. **Redémarrez VS Code** pour activer l'extension

### Vérification

Après redémarrage, l'extension doit démarrer automatiquement le proxy sur le port **3099**.
Vous pouvez vérifier via la palette de commandes : `Ctrl+Shift+P` → `MAX: Statut du proxy Copilot`

---

## Étape 3 — Vérifier la configuration

Le fichier de configuration se trouve dans `dev-conf-docker/config.env`.

```dotenv
NODE_ENV=development
PORT=8082

# Mode dev : bypass authentification JIRA (mettre false si connecté VPN)
DEV_MODE=true

# Proxy LLM — pointe vers l'extension VS Code installée à l'étape 2
LLM_BASE_URL=http://127.0.0.1:3099/v1
GITHUB_TOKEN=copilot-proxy
GITHUB_MODEL=gpt-5.4
```

> **DEV_MODE=true** : permet d'utiliser MAX sans VPN ni token JIRA (recommandé pour démarrer).
> **DEV_MODE=false** : à utiliser quand vous êtes connecté au VPN La Poste et souhaitez publier dans JIRA.

---

## Étape 4 — Installer les dépendances (une seule fois)

Ouvrez un terminal dans VS Code (`Ctrl+ù` ou `Terminal > Nouveau terminal`) et exécutez :

#Pour les POSTIERS Si on est sur site ça ne va pas marcher, il faut être chez soi

==> ** être chez toi et connecté en ZSCALER ! **

```Terminal powershell : Exécuter ces 3 commandes 

npm config set registry  https://registry.npmjs.org/
 
$env:NODE_OPTIONS="--tls-min-v1.2"
 
npm install --ignore-scripts --no-audit --verbose

```
  
``` [Si la commande npm install s'est terminé avec échec exécuter ces 2 commandes avant de recommencer l'étape 4

  npm cache clean --force
  Remove-Item -Recurse -Force node_modules
    ]

```

Attendez la fin de l'installation (quelques secondes).

---

## Étape 5 — Lancer le serveur MAX

Dans le terminal VS Code, exécutez la commande suivante :

```powershell
cd .\back-max\ ; clear; taskkill /f /im node.exe 2>$null; node server.js
```

> Cette commande :
> - Se place dans le dossier `back-max`
> - Nettoie les éventuels processus Node.js déjà en cours
> - Démarre le serveur MAX sur le port **8082**

**Résultat attendu dans le terminal :**
```
✅ MAX V6 démarré sur http://localhost:8082
📡 LLM connecté : http://127.0.0.1:3099/v1
🔧 Mode : development (DEV_MODE=true)
```

---

## Étape 6 — Accéder à MAX dans le navigateur

Ouvrez votre navigateur et accédez à :

```
http://localhost:8082
```

### En mode DEV_MODE=true (sans VPN) (Par défaut)
La page d'accueil s'ouvre directement sans demander de connexion.

### En mode DEV_MODE=false (avec VPN La Poste)
La page de connexion s'affiche — saisissez votre **Personal Access Token JIRA**.

> ⚠️ **Utilisateurs Externes (DiversIT)** : si vous voyez le bandeau *"veuillez configurer votre Proxy"* sur la page de connexion, assurez-vous d'avoir suivi la section **[Configuration du Proxy](#configuration-du-proxy-pour-utilisateurs-externes-diversit)** avant de saisir votre token.

**Obtenir un PAT JIRA :**
1. Connectez-vous à `https://jira.net.extra.laposte.fr/jira`
2. Cliquez sur votre avatar → **Profile** → **Personal Access Tokens**
3. Créez un token (nom : `MAX Application`, expiration : 90 jours)
4. Copiez-le — il ne s'affiche qu'une seule fois

---

## Étape 7 — Utiliser MAX

### Module 1 — SPECS Analyzer

Accessible via le bouton **Analyser des SPECS** depuis l'accueil.

| Action | Comment |
|--------|---------|
| Charger une SPECS | Glisser-déposer un `.md`, `.docx` ou `.pdf` |
| Charger depuis JIRA | Coller une clé JIRA (ex: `PROJ-123`) dans le champ |
| Coller du texte | Coller directement le contenu dans la zone de texte |
| Lancer l'analyse | Cliquer sur **Analyser** |
| Générer les US | Cliquer sur **Générer User Stories** après l'analyse |
| Exporter | Bouton **Télécharger .docx** ou copier dans le presse-papiers |

### Module 2 — Tests Generator

Accessible via le bouton **Générer des Tests** depuis l'accueil.

| Action | Comment |
|--------|---------|
| Charger des User Stories | Coller les US/CA ou charger un `.docx` |
| Charger depuis JIRA | Coller une clé JIRA de User Story |
| Générer les Gherkin | Cliquer sur **Générer les tests** |
| Publier dans JIRA | Cliquer sur **Publier dans JIRA** (confirmation demandée) |
| Exporter | Bouton **Télécharger .docx** ou copier dans le presse-papiers |

---

## Arrêter le serveur

Dans le terminal VS Code où le serveur tourne, appuyez sur :

```
Ctrl+C
```

Pour forcer l'arrêt de tous les processus Node.js si nécessaire :

```powershell
taskkill /f /im node.exe
```

---

## Résolution des problèmes fréquents

| Symptôme | Cause probable | Solution |
|----------|---------------|----------|
| `EADDRINUSE: port 8082` | Un serveur MAX tourne déjà | Relancer avec la commande complète (elle tue les processus existants) |
| `Cannot connect to LLM` | Le proxy VS Code n'est pas actif | Vérifier que l'extension est installée et VS Code redémarré |
| Réponses IA vides ou erreur LLM | GitHub Copilot non connecté | VS Code → Comptes → vérifier la connexion Copilot |
| Page blanche sur `localhost:8082` | Serveur non démarré | Vérifier le terminal — relancer l'étape 5 |
| Erreur JIRA 401 | Token expiré ou invalide | Générer un nouveau PAT JIRA |
| Module Cucumber inaccessible | `back-cucumber` non démarré | Vérifier les logs dans le terminal (spawn automatique) |
| Impossible de joindre JIRA (DiversIT) | Proxy réseau non configuré | Suivre la section **Configuration du Proxy pour Utilisateurs Externes** |
| Erreur SSL / certificat JIRA (DiversIT) | Proxy SSL interception | Ajouter `http.proxyStrictSSL: false` dans les paramètres VS Code |

---


## ==============================
## Procédure de désinstallation
## ==============================


### Étape 1 — Arrêter le serveur MAX

Si le serveur MAX est en cours d'exécution, arrêtez-le d'abord :

```powershell
taskkill /f /im node.exe
```

### Étape 2 — Désinstaller l'extension MAX Copilot Proxy

#### Via la palette de commandes VS Code (recommandé)

1. Ouvrez la palette : `Ctrl+Shift+P`
2. Tapez : `Extensions: Show Installed Extensions`
3. Recherchez **MAX Copilot Proxy** dans la liste
4. Cliquez sur l'icône de désinstallation (poubelle)
5. **Redémarrez VS Code** pour finaliser la suppression

#### Via le terminal externe à VSCODE

```powershell
code --uninstall-extension max-copilot-proxy
```

### Étape 3 — Supprimer les dépendances Node.js

Pour libérer l'espace disque occupé par les modules installés :

```powershell
# Depuis la racine du projet MAX
Remove-Item -Recurse -Force .\back-max\node_modules
```

> Si d'autres sous-services ont été utilisés, répétez pour chaque dossier concerné :
> `back-max\services\specs\`, `back-max\services\tests\`, etc.

### Étape 4 — Supprimer le dossier du projet (optionnel)

> ⚠️ **Attention** : Cette action est irréversible. Sauvegardez vos données avant de procéder.

Si vous souhaitez supprimer complètement le projet MAX de votre poste :

1. Fermez VS Code
2. Supprimez le dossier `MAX_V6` via l'Explorateur Windows ou via PowerShell :

```powershell
Remove-Item -Recurse -Force "C:\chemin\vers\MAX_V6"
```

### Étape 5 — Nettoyer la configuration VS Code (optionnel)

Si vous avez configuré des paramètres spécifiques à MAX dans VS Code :

1. Ouvrez `Ctrl+Shift+P` → `Preferences: Open Settings (JSON)`
2. Supprimez les entrées relatives à `max-copilot-proxy` si présentes

---

## Commande de référence rapide

```powershell
# Lancer MAX (à exécuter depuis la racine du projet dans le terminal VS Code)
cd .\back-max\ ; clear; taskkill /f /im node.exe 2>$null; node server.js
```

```
URL d'accès : http://localhost:8082
```
