# backend/Dockerfile

FROM python:3.12

# Définir un répertoire de travail
WORKDIR /app

# Installer les dépendances système utiles
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copier les fichiers Python
COPY ./requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source de l’app
COPY . .

# Exposer le port de l'API
EXPOSE 8000

# Commande pour lancer FastAPI avec auto-reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
