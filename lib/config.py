import os
from pathlib import Path
from dotenv import load_dotenv

# Carpeta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables desde .env
load_dotenv(BASE_DIR / ".env")

# Configuración principal
KEYS_URL = os.getenv("KEYS_URL")
DISTRO = os.getenv("DISTRO", "linux")

MODELS_DIR = BASE_DIR / os.getenv("MODELS_DIR", "models")
KEYS_DIR = BASE_DIR / os.getenv("KEYS_DIR", "keys")

# Archivo keys.json
KEYS_FILE = KEYS_DIR / "keys.json"

# Crear carpetas necesarias si no existen
MODELS_DIR.mkdir(parents=True, exist_ok=True)
KEYS_DIR.mkdir(parents=True, exist_ok=True)
