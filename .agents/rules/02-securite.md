---
trigger: always_on
---

# Regle : securite (activation : Always On)
- Ne jamais ecrire de cle API, mot de passe ou token dans un fichier versionne.
- Toute entree venant du navigateur ou du LLM est validee par un schema Pydantic.
- Tout chemin de fichier est resolu puis verifie : il doit rester dans le dossier sandbox.
- Les requetes SQL sont parametrees (jamais de concatenation de texte).
- Le CORS n'autorise que les origines listees dans .env.
- Avant toute action qui supprime ou modifie des donnees : demander confirmation a l'utilisateur.
