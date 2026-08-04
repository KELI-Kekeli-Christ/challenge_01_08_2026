# 🚀 Système de Recommandation : Dépôts GitHub

Ce projet est une solution proposée pour le **Challenge 01/08/2026**.
Il implémente un système de recommandation de **Dépôts GitHub** basé sur le traitement du langage naturel (NLP) via TF-IDF et la Similarité Cosinus.

## 🎯 Objectif du Challenge
L'objectif initial était de comprendre un code existant (qui recommandait des films à partir de listes d'acteurs) et de l'adapter à un nouveau contexte.
Pour ce faire, j'ai choisi de construire un tout nouveau jeu de données à partir de l'**API GitHub** et d'améliorer drastiquement les mathématiques sous-jacentes du modèle original.

## 📊 Dataset : `github_repositories.csv`
Le dossier `data/` contient maintenant un jeu de données extrait dynamiquement (via le script `fetch_github.py` ajouté au projet) contenant 500 dépôts GitHub très populaires (ayant plus de 5000 étoiles).
Les colonnes clés combinées pour générer des recommandations sont :
- `description` : Le résumé narratif du projet.
- `language` : Le langage de programmation principal.
- `topics` : Les tags (labels) associés au dépôt.

## 🛠️ Améliorations de l'Algorithme (Notebook)
Le notebook `recomendation.ipynb` a été mis à jour avec les améliorations suivantes :

1. **Extraction Textuelle via TF-IDF** : Au lieu de construire un vocabulaire binaire manuel (qui compte simplement la présence d'un mot), le modèle utilise désormais le `TfidfVectorizer` (scikit-learn). Cela pénalise les termes trop fréquents (ex: 'software', 'tool') et valorise les mots-clés spécifiques et identifiants (ex: 'kubernetes', 'react').
2. **Similarité Cosinus (Cosine Similarity)** : Le code original utilisait un simple produit scalaire sur des vecteurs non normalisés, ce qui avantageait artificiellement les films/éléments ayant le plus de métadonnées, peu importe la similarité réelle. En passant à la Similarité Cosinus, l'algorithme normalise les données et calcule l'angle entre les vecteurs, offrant un score précis entre `0` et `1`.

## 🚀 Comment tester localement
1. Assurez-vous d'avoir installé les dépendances requises :
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
2. Ouvrez le notebook `recomendation.ipynb` dans votre environnement préféré (Jupyter, VS Code) et exécutez l'ensemble des cellules pour voir l'algorithme recommander des dépôts similaires !
