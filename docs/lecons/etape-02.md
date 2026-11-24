# Leçon — Étape 02 : Environnement Python & squelette FastAPI

## Notions clés (en 2 phrases)
- **Environnement virtuel (`.venv`)** : C'est une boîte isolée qui contient uniquement les bibliothèques Python de ce projet. Cela évite les conflits de versions entre différents projets sur ton ordinateur.
- **CORS (Cross-Origin Resource Sharing)** : C'est une règle de sécurité des navigateurs qui bloque par défaut les requêtes venant d'une autre adresse (origine) que le serveur. On configure donc explicitement la liste des origines autorisées dans `.env`.

### Analogie
Imagine un immeuble (ton serveur FastAPI) :
- `.venv` est l'appartement dédié au projet MIA avec ses propres meubles (paquets Python).
- `config.py` est le carnet d'instructions à l'entrée.
- Le **CORS** est le gardien qui vérifie la liste des visiteurs autorisés (`CORS_ORIGINS`).
- `/health` est l'interphone : tu appuies dessus, il répond `"ok"` pour prouver que quelqu'un est là.

---

## Les fichiers créés

### 1. `requirements.txt`
- **Rôle** : Liste les paquets Python nécessaires au projet avec des versions encadrées (`fastapi`, `uvicorn`, `pydantic-settings`, `pytest`, `httpx`).
- **Pourquoi ce choix** : Garder la liste courte et légère pour le ThinkPad X390 (8 Go de RAM). `httpx` est nécessaire à `TestClient` de FastAPI pour exécuter les tests sans lancer de vrai serveur.
- **Erreurs fréquentes** : Installer des paquets globalement sans activer `.venv`, ou oublier d'ajouter un nouveau paquet dans `requirements.txt`.

### 2. `backend/config.py`
- **Rôle** : Charge automatiquement les variables du fichier `.env` dans un objet Python typé (`settings`).
- **Pourquoi ce choix** : `pydantic-settings` valide les types dès le démarrage et évite d'éparpiller des `os.getenv(...)` partout dans le code (principe DRY).
- **Erreurs fréquentes** : Mettre une vraie clé API comme valeur par défaut dans `config.py`. Les secrets doivent rester vides par défaut et n'exister que dans `.env`.

### 3. `backend/main.py`
- **Rôle** : Point d'entrée du serveur FastAPI, configuration du middleware CORS et première route `GET /health`.
- **Pourquoi ce choix** : `response_model=HealthResponse` garantit avec Pydantic v2 que la réponse JSON respecte toujours le format attendu.
- **Erreurs fréquentes** : Mettre `allow_origins=["*"]` en production (faille de sécurité, interdit par `02-securite.md`).

### 4. `tests/test_health.py`
- **Rôle** : Vérifie automatiquement que `GET /health` renvoie un code HTTP `200` et le bon JSON.
- **Pourquoi ce choix** : Tester tôt avec `pytest` permet de repérer immédiatement si une modification casse le serveur.
- **Erreurs fréquentes** : Ne pas nommer le fichier `test_*.py` ou la fonction `test_*`, ce qui empêche `pytest` de détecter le test.

---

## Ce que j'ai appris
- Isoler les dépendances d'un projet Python avec `.venv` et `requirements.txt`.
- Centraliser et valider la configuration `.env` avec `pydantic-settings`.
- Créer une première route FastAPI typée avec Pydantic v2 et la tester avec `pytest`.

## Erreurs fréquentes à retenir
1. Oublier d'activer `.venv` avant de lancer `uvicorn` ou `pytest`.
2. Laisser `allow_origins=["*"]` dans le CORS au lieu de lire `.env`.
3. Oublier `__init__.py` dans `backend/`, ce qui peut empêcher Python de reconnaître le dossier comme un package.

---

## Mini exercice (avec correction)

**Question** : Tu veux ajouter une route `GET /version` dans `backend/main.py` qui renvoie `{"version": "0.1.0"}` en utilisant un modèle Pydantic `VersionResponse`. Comment l'écris-tu ?

<details>
<summary>Voir la correction</summary>

```python
class VersionResponse(BaseModel):
    version: str


@app.get("/version", response_model=VersionResponse)
def get_version() -> VersionResponse:
    return VersionResponse(version="0.1.0")
```

</details>
