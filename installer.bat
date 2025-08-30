@echo off
setlocal

echo 🪟 Detectado Windows
echo ➡️ Instalando dependencias con winget...

:: comprobar que winget está disponible
where winget >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ❌ winget no está disponible. Instala manualmente Python, Git y Docker Desktop.
    exit /b 1
)

:: instalar dependencias
:: winget install -e --id Python.Python.3 -h
:: winget install -e --id Git.Git -h
:: winget install -e --id Docker.DockerDesktop -h

:: =========================
:: 📂 Preparar estructura
:: =========================
set INSTALL_DIR=%USERPROFILE%\opcean-cli
mkdir %INSTALL_DIR%
cd %INSTALL_DIR%

mkdir models lib funcs keys

:: =========================
:: 🌐 Descargar archivos
:: =========================
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

:: =========================
:: 🐍 Python + venv
:: =========================
py -3 -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt

:: =========================
:: ⚙️ Configuración inicial
:: =========================
curl -O https://raw.githubusercontent.com/OpceanAI/Opcean-CLI/refs/heads/main/.example.env
copy .example.env .env

:: =========================
:: 🔗 Crear acceso rápido
:: =========================
echo @echo off > %USERPROFILE%\opceanai-cli.bat
echo cd %%USERPROFILE%%\opcean-cli >> %USERPROFILE%\opceanai-cli.bat
echo call venv\Scripts\activate >> %USERPROFILE%\opceanai-cli.bat
echo python main.py %%* >> %USERPROFILE%\opceanai-cli.bat

echo ✅ Instalación completada con éxito
echo Puedes ejecutar el CLI con: opceanai-cli.bat

endlocal
pause
