# Couche 1 — Image de base
FROM python:3.12-slim

# Couche 2 — Répertoire de travail dans le container
WORKDIR /app

# Couche 3 — Copie et installation des dépendances
# On copie UNIQUEMENT requirements.txt en premier pour profiter du cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Couche 4 — Copie du code source
COPY . .

# Couche 5 — Port exposé par le container
EXPOSE 8000

# Couche 6 — Commande de démarrage
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]