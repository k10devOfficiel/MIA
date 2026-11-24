# Leçon — Étape 01 : Initialisation du projet

## Objectif de l'étape
Poser des bases propres et sécurisées avant d'écrire la moindre ligne de code Python ou JavaScript.

---

## Les fichiers créés

### 1. `GEMINI.md`
- **Rôle** : Ce fichier contient le cahier des charges, les règles de qualité, la stack technique et les contraintes matérielles du projet.
- **Pourquoi ce choix** : Garder les règles à la racine du dépôt permet à toi (et à l'assistant IA) d'avoir toujours la même référence à chaque session.
- **Erreurs fréquentes** : Modifier la stack en cours de route sans mettre à jour ce fichier, ce qui crée des incohérences.

### 2. `.gitignore`
- **Rôle** : Indique à Git quels fichiers et dossiers il doit **ignorer** (ne jamais suivre ni envoyer sur GitHub).
- **Pourquoi ce choix** :
  - `.env` contient les mots de passe et clés API : il ne doit **jamais** finir dans Git.
  - `.venv/` et `__pycache__/` sont générés automatiquement par Python et sont lourds/inutiles dans un dépôt.
  - `*.db` / `*.sqlite` évitent de partager ta base de données personnelle.
- **Erreurs fréquentes** : Créer `.gitignore` *après* avoir déjà fait `git add .env`. Si un fichier est déjà suivi par Git, l'ajouter au `.gitignore` ne suffit plus : il faut le retirer du suivi Git (`git rm --cached .env`).

### 3. `.env.example`
- **Rôle** : C'est un **modèle** du futur fichier `.env`, sans aucune valeur secrète.
- **Pourquoi ce choix** : Comme `.env` est ignoré par Git, `.env.example` sert de documentation pour savoir quelles variables d'environnement le projet attend (ex. `OLLAMA_MODEL`, `CLOUD_API_KEY`).
- **Erreurs fréquentes** : Mettre sa vraie clé API dans `.env.example` par inadvertance. Ce fichier est public dans Git : les clés doivent rester vides dedans.

### 4. `README.md`
- **Rôle** : La page d'accueil du projet (résumé, stack technique, où trouver les leçons).
- **Pourquoi ce choix** : Tout projet professionnel commence par un `README.md` clair pour qu'une autre personne (ou toi dans 6 mois) comprenne le projet en 10 secondes.
- **Erreurs fréquentes** : Ne jamais le maintenir à jour au fil de l'avancement.

---

## Récapitulatif sécurité
- **Règle d'or** : `.env` = privé (ignoré par Git) ; `.env.example` = modèle sans secret (suivi par Git).
