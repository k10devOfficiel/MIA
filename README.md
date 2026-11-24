# Projet MIA

**MIA** est une assistante IA avec une interface web animée (personnage chibi robot aux cheveux blancs, palette orange/rouge/noir), dotée de voix, d'écoute, de mémoire et d'outils fichiers sécurisés.

## Stack technique

- **Backend** : Python 3.11+, FastAPI, Pydantic v2, SQLite
- **Frontend** : HTML, CSS, JavaScript (modules ES), sans framework
- **IA** : abstraction `LLMProvider` (`OllamaProvider` en local avec `qwen2.5:3b` ou `qwen2.5:1.5b`, et `CloudProvider` en ligne)

## Documentation pédagogique

Chaque étape du projet est expliquée dans `docs/lecons/`.
