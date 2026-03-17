# Dépannage rapide

## Erreur `ModuleNotFoundError: No module named src`
Lancer les scripts Python depuis la racine du projet avec :

```bash
python -m src.dbapi.main
python -m src.core.main
python -m src.orm.main
```

## Erreur `mysql: command not found` dans Codespaces
Exécuter :

```bash
bash scripts/setup.sh
```

Le script installe automatiquement le client MySQL s'il manque.

## Erreur `Table ... doesn't exist`
Initialiser la base avec :

```bash
bash scripts/setup.sh
bash scripts/check_db.sh
```

En local, injecter aussi `sql/01_schema.sql` puis `sql/02_seed.sql`.
