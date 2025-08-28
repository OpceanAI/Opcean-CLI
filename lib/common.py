import subprocess
from rich.console import Console

console = Console()

def run_command(cmd, cwd=None):
    """Ejecuta un comando en shell mostrando output bonito"""
    process = subprocess.Popen(cmd, shell=True, cwd=cwd,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True)
    for line in process.stdout:
        console.print(f"[cyan]|[/cyan] {line.strip()}")
    process.wait()
    return process.returncode