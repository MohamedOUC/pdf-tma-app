#!/bin/bash

# Crée les dossiers
mkdir -p backend/app/routes
mkdir -p frontend/src/components
mkdir -p frontend/src/views
mkdir -p docs/incidents
mkdir -p docs/evolutions

# Crée les fichiers backend
touch backend/app/__init__.py
touch backend/app/main.py
touch backend/app/models.py
touch backend/app/schemas.py
touch backend/app/database.py
touch backend/app/config.py
touch backend/app/routes/__init__.py
touch backend/app/routes/documents.py
touch backend/app/routes/ged.py
touch backend/.env
touch backend/requirements.txt
touch backend/Dockerfile

# Crée les fichiers frontend
touch frontend/src/components/DocumentForm.vue
touch frontend/src/views/Dashboard.vue
touch frontend/src/App.vue
touch frontend/src/main.js
touch frontend/src/router.js
touch frontend/Dockerfile
touch frontend/package.json  # (sera écrasé par npm init plus tard)

# Crée les fichiers Docker, README, git
touch docker-compose.yml
touch .gitignore
touch README.md
touch LICENSE

# Crée les docs
touch docs/architecture.md
touch docs/support-utilisateur.md
touch docs/tma-n1-n2.md
touch docs/incidents/incident-connexion-db.md
touch docs/incidents/bug-creation-document.md
touch docs/evolutions/ajout-recherche-doc.md
touch docs/evolutions/refactor-doc-api.md

echo "✅ Arborescence et fichiers créés !"

