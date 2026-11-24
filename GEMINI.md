# Projet MIA
MIA est une assistante IA avec interface web animee (personnage chibi robot, cheveux blancs, couleurs orange/rouge/noir), voix, ecoute, memoire et outils fichiers.

## Utilisateur
Etudiant en BTS IDA, niveau debutant-intermediaire. Objectif : comprendre chaque ligne de code et savoir la reproduire seul.

## Stack
- Backend : Python 3.11+, FastAPI, Pydantic v2, SQLite
- Frontend : HTML / CSS / JavaScript (modules ES), sans framework au depart
- IA : classe abstraite LLMProvider avec OllamaProvider (local) et CloudProvider (en ligne)

## Materiel cible
ThinkPad X390, 8 Go de RAM, CPU seul, pas de GPU. Modele local leger (qwen2.5:3b, repli qwen2.5:1.5b). Eviter toute dependance lourde.

## Regles de travail
- Toujours proposer un plan et attendre ma validation avant de coder.
- Une seule etape a la fois. Ne jamais anticiper les etapes suivantes.
- Expliquer chaque fichier cree, en francais simple, dans docs/lecons/etape-XX.md : role, pourquoi ce choix, erreurs frequentes.
- Terminer chaque etape par : comment tester, un mini exercice avec correction, un message de commit.

## Qualite
SOLID, DRY, KISS, Clean Code. Noms explicites, fonctions courtes, type hints partout, commentaires seulement s'ils apportent de la valeur.

## Securite
- Secrets uniquement dans .env, jamais dans le code ni dans Git.
- Valider toute entree avec Pydantic. Ne jamais faire confiance a la sortie du LLM.
- Fichiers : sandbox obligatoire, corbeille au lieu de suppression, confirmation utilisateur.

## Interdit
Aucune commande destructrice (suppression, formatage, git push --force) sans demande explicite. Aucun paquet installe sans justification.
