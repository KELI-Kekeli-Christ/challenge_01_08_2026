# Challenge 01/08/2026

Ce dépôt contient un mini projet de recommandation basé sur un jeu de données de films fourni dans le dossier data.

## Objectif du challenge

Le but du challenge n’est pas de tout réinventer. L’idée est plutôt de comprendre le code existant, d’adapter une solution de recommandation à un contexte différent, et de montrer que l’on sait travailler avec des données réelles en les transformant pour qu’un algorithme puisse les utiliser.

En pratique, au lieu de se limiter aux données de film déjà utilisées ici, on peut essayer d’utiliser une autre source de données pertinente, puis adapter le code pour qu’il fonctionne avec cette nouvelle source.

> Une bonne lecture du code est importante : si on le comprend vraiment bien, il se peut qu’il contienne une erreur ou un point à améliorer.

## Structure du dépôt

- [data/](data/) : contient le jeu de données utilisé par le notebook.
- [recomendation.ipynb](recomendation.ipynb) : notebook principal contenant la logique de recommandation.
- [README.md](README.md) : ce fichier d’explication.

### Contenu du dossier data

Le dossier [data/](data/) contient actuellement :

- [data/tmdb_5000_credits.csv](data/tmdb_5000_credits.csv)

Ce fichier contient des informations de films avec notamment :

- movie_id : identifiant du film
- title : titre du film
- cast : liste des acteurs
- crew : liste des membres de l’équipe de production

Ces colonnes servent de base à la recommandation actuelle.

### Contenu du notebook de recommandation

Le notebook [recomendation.ipynb](recomendation.ipynb) fait les actions suivantes :

1. Charge le fichier CSV depuis [data/tmdb_5000_credits.csv](data/tmdb_5000_credits.csv)
2. Lit et parse les colonnes cast et crew
3. Construit des vecteurs de caractéristiques à partir des personnes présentes dans ces colonnes
4. Calcule une similarité entre films avec un produit scalaire sur ces vecteurs
5. Retourne une liste de films recommandés à partir d’un titre donné

## Comment forker le dépôt

1. Ouvrez la page GitHub du dépôt.
2. Cliquez sur le bouton Fork en haut à droite.
3. Choisissez votre compte GitHub comme destination.
4. Une fois le fork créé, clonez votre copie locale :

```bash
git clone https://github.com/VOTRE_NOM_UTILISATEUR/challenge_01_08_2026.git
cd challenge_01_08_2026
```

## Comment travailler localement

Avant de commencer, créez une branche de travail :

```bash
git checkout -b feature/ma-proposition
```

Puis faites vos modifications, ajoutez les fichiers et validez :

```bash
git add .
git commit -m "Ajout de ma solution"
```

Enfin, poussez la branche sur votre fork :

```bash
git push origin feature/ma-proposition
```

## Comment ouvrir une Pull Request

1. Ouvrez votre fork sur GitHub.
2. Cliquez sur Compare & pull request.
3. Décrivez clairement ce que vous avez changé.
4. Expliquez votre approche de recommandation et les données utilisées.
5. Soumettez la pull request.

## Conseils importants

- Le but n’est pas de réécrire un système de recommandation complètement différent de zéro.
- Il faut surtout montrer que vous comprenez le flux de données et que vous savez l’adapter.
- Si vous changez de source de données, il faut aussi adapter la logique de préparation des caractéristiques.
- Une bonne compréhension du code peut révéler une erreur cachée ou un biais dans l’implémentation.

