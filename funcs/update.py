import requests
from pathlib import Path
from rich.console import Console

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent
KEYS_FILE = BASE_DIR / "keys.json"

def update(url: str):
    """Descarga keys.json desde la URL dada"""
    console.print("[yellow]→ Descargando keys.json...[/yellow]")
    r = requests.get(url)
    r.raise_for_status()
    KEYS_FILE.write_text(r.text, encoding="utf-8")
    console.print("[green]✔ keys.json actualizado[/green]")
