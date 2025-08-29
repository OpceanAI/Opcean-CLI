#!/bin/sh

# =========================
# 🔍 Detectar sistema
# =========================
OS="$(uname)"

if [ "$OS" = "Linux" ]; then
    if [ -f /etc/arch-release ]; then
        echo "🐧 Detectado Arch Linux"
        sudo pacman -Syu --noconfirm
        sudo pacman -S sudo python3 docker docker-compose make git curl --noconfirm
    elif [ -f /etc/debian_version ]; then
        echo "🐧 Detectado Ubuntu/Debian"
        sudo apt update && sudo apt upgrade -y
        sudo apt install -y python3 python3-venv docker.io docker-compose make git curl
    else
        echo "⚠️ Distro Linux no soportada aún"
        exit 1
    fi

    # añadir usuario al grupo docker
    sudo usermod -aG docker "$USER"
else
    echo "❌ Este instalador (.sh) es solo para Linux"
    echo "➡️ Usa el archivo installer.bat en Windows"
    exit 1
fi

# =========================
# 📂 Preparar estructura
# =========================
INSTALL_DIR="/opt/opcean-cli"

sudo mkdir -p "$INSTALL_DIR"
sudo chown -R "$USER":"$USER" "$INSTALL_DIR"

cd "$INSTALL_DIR"

mkdir -p models lib funcs keys

# =========================
# 🌐 Descargar archivos
# =========================
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/requirements.txt
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/main.py

cd lib
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/lib/common.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/lib/config.py
cd ..

cd funcs
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/install.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/run.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/remove.py
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/funcs/update.py
cd ..

# =========================
# 🐍 Python + venv
# =========================
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# =========================
# ⚙️ Configuración inicial
# =========================
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/.example.env
cp .example.env .env

# =========================
# 🔗 Enlace simbólico / acceso rápido
# =========================
echo '#!/bin/bash
cd /opt/opcean-cli
source venv/bin/activate
python3 main.py "$@"' | sudo tee /usr/local/bin/opceanai-cli > /dev/null

sudo chmod +x /usr/local/bin/opceanai-cli

echo "🎉 Instalación completada con éxito"
