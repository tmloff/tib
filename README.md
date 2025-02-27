# TIB - Transfer, Integrate, Backup

TIB (Transfer, Integrate, Backup) est un projet open-source conçu pour simplifier la collaboration en permettant de créer des sauvegardes de bases de données et de les restaurer sur une autre machine. L'application repose sur un système de commandes permettant d'effectuer ces actions de manière efficace. Elle est conçue pour être liée à un repository afin de faciliter la gestion des versions et des partages.

## Fonctionnalités principales

- **Sauvegarde et restauration** : créez des backups de vos bases de données et restaurez-les sur une autre machine en toute simplicité.
- **Collaboration optimisée** : facilite le travail d'équipe en assurant une synchronisation efficace des bases de données.
- **Système de commandes dédié** : offre des fonctionnalités permettant d'exécuter des opérations de sauvegarde et de restauration.
- **Intégration avec un repository** : permet de versionner et partager les sauvegardes via un dépôt distant.

## Technologies utilisées

Ce projet est développé en Python et repose sur les bibliothèques suivantes :

- `json` : pour la gestion des configurations et des données structurées.
- `subprocess` : pour l'exécution de commandes système liées à la gestion des bases de données.
- `os` : pour la gestion des fichiers et des interactions avec le système d'exploitation.

## Installation

1. Clonez le dépôt :
   ```sh
   git clone https://github.com/votre-utilisateur/TIB.git
   cd TIB
   ```

2. Assurez-vous d'avoir Python installé (version 3.x recommandée).

3. Installez les dépendances si nécessaire :
   ```sh
   pip install -r requirements.txt
   ```

## Utilisation

Lancez le script principal :
```sh
python main.py
```

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à proposer des améliorations via des issues ou des pull requests.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.