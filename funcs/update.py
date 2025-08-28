import requests
from pathlib import Path
from rich.console import Console
from lib import config

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
KEYS_FILE = BASE_DIR / "keys.json"

def update():
    """Descarga keys.json desde la URL dada en .env"""
    console.print("[yellow]→ Descargando keys.json...[/yellow]")
    r = requests.get(config.KEYS_URL)
    r.raise_for_status()
    config.KEYS_FILE.write_text(r.text, encoding="utf-8")
    console.print(f"[green]✔ keys.json actualizado en {config.KEYS_FILE}[/green]")