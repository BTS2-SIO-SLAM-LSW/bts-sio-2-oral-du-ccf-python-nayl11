# Option 2 - Installation locale

Ce guide décrit l'installation complète sur Windows, Linux, macOS et WSL.

## Outils nécessaires pour le CCF
- Git ;
- Python 3.11 ou version proche ;
- pip ;
- un environnement virtuel Python ;
- MySQL 8.x avec client `mysql` ;
- un terminal adapté au système ;
- l'éditeur PlantUML en ligne : `https://editor.plantuml.com/` ;
- éventuellement Visual Studio Code pour éditer les fichiers du projet.

## 1. Clonage du dépôt
```bash
git clone <url-du-depot>
cd ccf_boutikpro_codespaces
```

## 2. Choix du script selon le système
- Windows CMD : `scripts/local/setup_windows.bat`
- Windows PowerShell : `scripts/local/setup_windows.ps1`
- Linux : `bash scripts/local/setup_linux.sh`
- macOS : `bash scripts/local/setup_macos.sh`
- WSL : `bash scripts/local/setup_wsl.sh`

Ces scripts préparent le projet local : environnement virtuel, dépendances Python et fichier `.env`.

## 3. Configuration de la base MySQL
Créer la base `boutikpro_ccf`, puis exécuter les scripts SQL dans cet ordre :

```bash
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS boutikpro_ccf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p boutikpro_ccf < sql/01_schema.sql
mysql -u root -p boutikpro_ccf < sql/02_seed.sql
```

Adapter ensuite le fichier `.env` à votre installation locale.

Exemple local typique :

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=boutikpro_ccf
DB_USER=root
DB_PASSWORD=votre_mot_de_passe
```

## 4. PlantUML
Utiliser la version recommandée en ligne :

```text
https://editor.plantuml.com/
```

Copier ensuite le contenu final dans `uml/usecase.puml`.

## 5. Lancement des squelettes Python
Toujours depuis la racine du projet et après activation de l'environnement virtuel :

```bash
python -m src.dbapi.main
python -m src.core.main
python -m src.orm.main
```

## 6. Consignes spécifiques par système

### Windows (.bat)
- Ouvrir **Invite de commandes**.
- Se placer dans le dépôt.
- Lancer :

```bat
scripts\local\setup_windows.bat
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS boutikpro_ccf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p boutikpro_ccf < sql\01_schema.sql
mysql -u root -p boutikpro_ccf < sql\02_seed.sql
.venv\Scripts\activate.bat
python -m src.dbapi.main
```

### Windows (.ps1)
- Ouvrir **PowerShell**.
- Autoriser l'exécution locale si nécessaire.
- Lancer :

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\local\setup_windows.ps1
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS boutikpro_ccf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
cmd /c "mysql -u root -p boutikpro_ccf < sql\01_schema.sql"
cmd /c "mysql -u root -p boutikpro_ccf < sql\02_seed.sql"
.\.venv\Scripts\Activate.ps1
python -m src.dbapi.main
```

### Linux
- Ouvrir un terminal.
- Lancer :

```bash
bash scripts/local/setup_linux.sh
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS boutikpro_ccf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p boutikpro_ccf < sql/01_schema.sql
mysql -u root -p boutikpro_ccf < sql/02_seed.sql
source .venv/bin/activate
python -m src.dbapi.main
```

### macOS
- Ouvrir Terminal.
- Lancer :

```bash
bash scripts/local/setup_macos.sh
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS boutikpro_ccf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p boutikpro_ccf < sql/01_schema.sql
mysql -u root -p boutikpro_ccf < sql/02_seed.sql
source .venv/bin/activate
python -m src.dbapi.main
```

### WSL
- Ouvrir votre distribution WSL.
- Installer MySQL côté Windows ou côté WSL selon votre organisation.
- Lancer :

```bash
bash scripts/local/setup_wsl.sh
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS boutikpro_ccf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p boutikpro_ccf < sql/01_schema.sql
mysql -u root -p boutikpro_ccf < sql/02_seed.sql
source .venv/bin/activate
python -m src.dbapi.main
```

## Rappel important
Ne pas lancer :

```bash
python src/dbapi/main.py
```

Préférer :

```bash
python -m src.dbapi.main
```

Le même principe s'applique à `src.core.main` et `src.orm.main`.


## 7. Installation facultative de Looping
Looping est un logiciel de modélisation de données qui peut être utilisé pour représenter un MCD et préparer le passage au MLD. Son installation est facultative.

Guide d'utilisation :
- [docs/guides/LOOPING.md](guides/LOOPING.md)

### Windows (.bat)
Exemple de lancement d'un installateur :

```bat
@echo off
set INSTALLER=C:\chemin\vers\LoopingSetup.exe
if exist "%INSTALLER%" (
    start "" "%INSTALLER%"
) else (
    echo Installateur non trouvé : %INSTALLER%
)
```

### Windows (.ps1)
Exemple PowerShell :

```powershell
$installer = "C:\chemin\vers\LoopingSetup.exe"
if (Test-Path $installer) {
    Start-Process -FilePath $installer
} else {
    Write-Host "Installateur non trouvé : $installer"
}
```

### Linux
Si vous disposez d'un exécutable ou d'un fichier Java :

```bash
chmod +x /chemin/vers/looping
/chemin/vers/looping
```

ou :

```bash
java -jar /chemin/vers/looping.jar
```

### macOS
Si vous disposez d'une application compatible :

```bash
open /chemin/vers/Looping.app
```

### WSL
Pour WSL, il est généralement plus simple de lancer Looping côté Windows :

```bash
cmd.exe /c start "" "C:\chemin\vers\LoopingSetup.exe"
```

Sinon, utilisez une version Java / Linux si votre environnement graphique WSL le permet.
