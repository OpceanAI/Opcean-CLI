.PHONY: install run

REPO_URL=https://github.com/OpceanAI/Archan-Open-source-
PKG_DIR=Archan-Open-source-

install:
	@echo "🐾 Clonando el repositorio..."
	@git clone $(REPO_URL) $(PKG_DIR) || echo "✔ Repo ya existe"
	@echo "🐳 Creando .env..."
	@cd $(PKG_DIR) && touch .env
	@echo "🐳 Construyendo y levantando Docker..."
	@cd $(PKG_DIR) && docker-compose up --build -d
	@cd $(PKG_DIR) && docker-compose down --volumes
	@echo "✅ Instalación completada (imagen guardada, contenedores borrados)"

run:
	@cd $(PKG_DIR) && docker-compose up -d

run-local:
	@echo "🐾 Ejecutando en local (sin Docker)..."
	# añade instrucciones para su ejecucion en local