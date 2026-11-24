# Leçon — Étape 03 : Configuration et serveur minimal

## Notions clés (en 2 phrases)
- **Serveur** : Un programme qui tourne en continu et attend des requêtes réseau (ici `uvicorn` qui exécute notre application FastAPI sur le port `8000`).
- **API (Application Programming Interface)** : Un ensemble d'adresses (routes) comme `GET /health` qui permettent à un client (le navigateur ou le frontend) de dialoguer avec le serveur en échangeant du JSON.
- **Fichier `.env`** : Un fichier texte local (ignoré par Git) qui stocke les réglages et secrets de l'application (`CLOUD_API_KEY`, `OLLAMA_MODEL`, `ALLOWED_ORIGINS`).
- **Validation de configuration** : Vérifier automatiquement dès le démarrage que chaque variable a le bon type et une valeur autorisée (ex. `LLM_PROVIDER` ne peut être que `"ollama"` ou `"cloud"`).

### Analogie
Imagine un restaurant :
- Le **serveur** (`uvicorn`), c'est le bâtiment ouvert qui accueille les clients.
- L'**API** (`FastAPI`), c'est la carte du menu : elle liste exactement ce qu'on peut commander (`GET /health`).
- Le fichier **`.env`**, c'est le classeur secret du gérant (code du coffre, fournisseur choisi, liste des VIP autorisés).
- **Pydantic Settings**, c'est le contrôle qualité avant l'ouverture : si le gérant a écrit un nom de fournisseur qui n'existe pas, le restaurant refuse d'ouvrir tout de suite avec un message d'erreur clair plutôt que de planter en plein service.

---

## Les fichiers créés ou modifiés

### 1. `backend/app/core/config.py`
- **Rôle** : Définit la classe `Settings` (héritée de `BaseSettings`) qui charge `.env` et valide chaque champ.
- **Pourquoi ce choix** : Utiliser `Literal["ollama", "cloud"]` empêche une faute de frappe (ex. `"olama"`) de passer silencieusement. La propriété `allowed_origins_list` transforme proprement la chaîne `ALLOWED_ORIGINS` en liste Python.
- **Erreurs fréquentes** : Oublier `extra="ignore"` (si `.env` contient d'anciennes variables, Pydantic lèverait une erreur), ou mettre une vraie clé API comme valeur par défaut.

### 2. `backend/app/main.py`
- **Rôle** : Crée l'instance `FastAPI`, configure le middleware **CORS restrictif** depuis `settings.allowed_origins_list` et expose `GET /health`.
- **Pourquoi ce choix** : Un CORS restrictif empêche un site malveillant externe d'appeler ton API locale. `response_model=HealthResponse` garantit un format JSON strict.
- **Erreurs fréquentes** : Écrire `allow_origins=["*"]` par facilité — c'est une faille de sécurité interdite par `02-securite.md`.

### 3. `.env.example`
- **Rôle** : Modèle documenté de toutes les variables attendues par `Settings`, sans aucune valeur secrète.
- **Pourquoi ce choix** : Permet de recréer un `.env` propre en quelques secondes.

### 4. `tests/test_health.py`
- **Rôle** : Teste automatiquement la route `GET /health` et vérifie que `Settings` rejette bien un `llm_provider` invalide.

---

## Ce que j'ai appris
- Différencier serveur (`uvicorn`), API (`FastAPI`) et configuration (`.env`).
- Valider des variables d'environnement avec `pydantic-settings` et `Literal`.
- Protéger son API avec un CORS restrictif lu depuis la configuration.

## Erreurs fréquentes à retenir
1. Mettre `allow_origins=["*"]` dans le CORS.
2. Lancer `uvicorn backend.main:app` au lieu de `uvicorn backend.app.main:app` (le bon chemin de module).
3. Écrire un secret dans `.env.example` ou `config.py`.

---

## Mini exercice (avec correction)

**Question** : Que se passe-t-il si tu mets `LLM_PROVIDER=openai` dans ton fichier `.env` et que tu lances le serveur ? Pourquoi est-ce une bonne chose ?

<details>
<summary>Voir la correction</summary>

Pydantic lève immédiatement une `ValidationError` au démarrage car `llm_provider` est typé `Literal["ollama", "cloud"]`.
C'est une bonne chose (**fail fast**) : tu repères l'erreur de configuration en 1 seconde au lancement, au lieu de découvrir un bug mystérieux plus tard pendant une conversation avec MIA.

</details>
