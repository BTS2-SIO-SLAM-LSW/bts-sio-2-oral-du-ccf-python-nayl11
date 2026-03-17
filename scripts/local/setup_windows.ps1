if (-not (Test-Path .venv)) {
    python -m venv .venv
}
& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
}
Write-Host "Projet local prepare."
Write-Host "Etape suivante : creer la base boutikpro_ccf puis injecter sql/01_schema.sql et sql/02_seed.sql."
Write-Host "Ensuite lancer python -m src.dbapi.main ou un autre mode."
