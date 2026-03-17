#!/usr/bin/env bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
[ -f .env ] || cp .env.example .env
echo "Projet local préparé."
echo "Étape suivante : créer la base boutikpro_ccf puis injecter sql/01_schema.sql et sql/02_seed.sql."
echo "Ensuite lancer python -m src.dbapi.main ou un autre mode."
