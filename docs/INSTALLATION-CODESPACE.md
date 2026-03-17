# Option 1 - Installation distante avec GitHub Codespaces

Ce mode d'installation utilise un environnement distant prêt à l'emploi.

## Outils nécessaires
- un compte GitHub ;
- GitHub Codespaces activé pour votre compte ;
- un navigateur Web moderne ;
- l'éditeur PlantUML en ligne : `https://editor.plantuml.com/`.

## Important
Dans le Codespace, le client MySQL n'est pas toujours disponible immédiatement dans le terminal.
Le script `scripts/setup.sh` installe automatiquement le client MySQL s'il manque, attend que le conteneur de base soit prêt, puis injecte `sql/01_schema.sql` et `sql/02_seed.sql`.

## Étapes
1. Créer un dépôt à partir du template.
2. Ouvrir le dépôt dans GitHub Codespaces.
3. Attendre la fin du build du conteneur.
4. Ouvrir un terminal à la racine du projet.
5. Exécuter :

```bash
bash scripts/setup.sh
bash scripts/check_db.sh
```

6. Vérifier que la commande précédente affiche bien les tables de la base `boutikpro_ccf`.
7. Lancer ensuite le mode Python choisi :

```bash
python -m src.dbapi.main
python -m src.core.main
python -m src.orm.main
```

## Ce que fait `scripts/setup.sh`
- installe `default-mysql-client` si `mysql` n'est pas encore disponible ;
- installe les dépendances Python ;
- attend que MySQL réponde sur l'hôte `db` ;
- charge `sql/01_schema.sql` ;
- charge `sql/02_seed.sql`.

## PlantUML en ligne
1. Ouvrir l'adresse suivante dans votre navigateur :

```text
https://editor.plantuml.com/
```

2. Copier le contenu de `uml/usecase.puml` dans l'éditeur en ligne.
3. Modifier le diagramme.
4. Recopier le résultat final dans votre fichier local `uml/usecase.puml` du dépôt.

## Vérifications recommandées
```bash
bash scripts/check_db.sh
python -m src.dbapi.main
python -m src.core.main
python -m src.orm.main
```

## Ne pas faire
Éviter de lancer directement :

```bash
python src/dbapi/main.py
python src/core/main.py
python src/orm/main.py
```

Les imports du projet sont prévus pour un lancement en mode module avec `python -m ...`.

## Ordre de travail conseillé
1. `START-HERE.md`
2. `docs/phase-01/01-diagramme-cas-utilisation.md`
3. `docs/guides/MCD_MLD.md`
4. `sql/student_upgrade.sql`
5. le mode Python choisi
