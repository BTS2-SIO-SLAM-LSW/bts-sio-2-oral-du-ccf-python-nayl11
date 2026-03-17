@echo off
setlocal
if not exist .venv (
  python -m venv .venv
)
call .venv\Scripts\activate.bat
pip install -r requirements.txt
if not exist .env copy .env.example .env

echo.
echo Projet local prepare.
echo Etape suivante : creer la base boutikpro_ccf puis injecter sql\01_schema.sql et sql\02_seed.sql.
echo Ensuite lancer python -m src.dbapi.main ou un autre mode.
endlocal
