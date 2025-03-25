# frontend/Dockerfile

FROM node:18

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste de l’app
COPY . .

# Exposer le port Vite (par défaut 5173)
EXPOSE 5173

# Lancer le serveur de dev Vite
CMD ["npm", "run", "dev", "--", "--host"]
