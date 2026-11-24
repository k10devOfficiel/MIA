---
trigger: model_decision
description: A charger pour tout travail sur frontend/ (style, accessibilite, animations, machine a etats)
---

# Regle : interface (activation : Model Decision, a charger pour tout travail sur frontend/)
- Style sobre et moderne inspire de Linear et Vercel : theme sombre, accents orange, beaucoup d'espace.
- Mobile-first et responsive. Contraste conforme WCAG AA.
- Accessibilite : aria-label, navigation clavier, focus visible, prefers-reduced-motion respecte.
- Animations en CSS (transform, opacity) uniquement, pas d'animation de layout.
- Le texte prononce par MIA est toujours affiche a l'ecran.
- Etat de MIA centralise dans un seul objet (machine a etats).
