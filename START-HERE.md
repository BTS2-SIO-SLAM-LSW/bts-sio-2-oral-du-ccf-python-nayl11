# START HERE

1. Choisir votre mode de travail :
   - Codespaces : lire `docs/INSTALLATION-CODESPACE.md`
   - Local : lire `docs/INSTALLATION-LOCALE.md`
2. Initialiser la base.
3. Vérifier les tables avec `bash scripts/check_db.sh` en Codespaces ou avec `mysql -u root -p boutikpro_ccf -e "SHOW TABLES;"` en local.
4. Réaliser le diagramme de cas d'utilisation dans `uml/usecase.puml`.
5. Choisir un mode Python et le lancer avec `python -m src.dbapi.main`, `python -m src.core.main` ou `python -m src.orm.main`.
