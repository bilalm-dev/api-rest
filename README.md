# API REST — FastAPI + PostgreSQL + JWT

Une API REST complète construite avec FastAPI, PostgreSQL et une authentification JWT. Projet réalisé en autonomie pour démontrer mes compétences en développement backend.

## Stack technique

- **Python 3.12** + **FastAPI** — framework web
- **PostgreSQL** — base de données relationnelle
- **SQLAlchemy** — ORM pour interagir avec la BDD
- **JWT** — authentification stateless
- **bcrypt** — hashing des mots de passe
- **Pytest** — tests d'intégration automatisés
- **Docker** + **Docker Compose** — containerisation
- **GitHub Actions** — pipeline CI/CD automatisé
- **Render** — déploiement cloud

## Fonctionnalités

- CRUD complet sur les utilisateurs
- Inscription et connexion avec JWT
- Routes protégées par token
- Documentation interactive auto-générée (Swagger)
- 5 tests d'intégration automatisés
- Containerisation complète avec Docker Compose
- Pipeline CI/CD automatisé — tests, build Docker, déploiement

## Demo

API disponible en ligne : [https://api-rest-4j5w.onrender.com/docs](https://api-rest-4j5w.onrender.com/docs)

Image Docker Hub : [bilalmdev164/api-rest](https://hub.docker.com/r/bilalmdev164/api-rest)

## Pipeline CI/CD

À chaque push sur `main` :

```
Push sur main
     │
     ▼
┌─────────┐     ┌──────────────┐     ┌──────────────┐
│  Tests  │ ──► │ Build Docker │ ──► │  Déploiement │
│ Pytest  │     │  + Push Hub  │     │    Render    │
└─────────┘     └──────────────┘     └──────────────┘
```

- **Tests** : lance PostgreSQL via service container et exécute les 5 tests d'intégration
- **Build Docker** : builde et pousse l'image taguée avec le hash du commit sur Docker Hub
- **Déploiement** : déclenche automatiquement le redéploiement sur Render

## Lancer le projet en local

### Prérequis
- Python 3.12+
- PostgreSQL

### Installation

```bash
# Cloner le repo
git clone https://github.com/bilalmdev164/api-rest.git
cd api-rest

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration

Crée un fichier `.env` à partir de l'exemple :

```bash
cp .env.example .env
# Remplis les variables dans .env
```

### Lancer le serveur

```bash
uvicorn app.main:app --reload
```

L'API est accessible sur `http://localhost:8000/docs`

### Lancer les tests

```bash
pytest tests/ -v
```

## Lancer avec Docker

### Prérequis
- Docker
- Docker Compose

### Installation

```bash
# Cloner le repo
git clone https://github.com/bilalmdev164/api-rest.git
cd api-rest

# Créer le fichier .env
cp .env.example .env
# Remplis les variables dans .env
```

### Lancer avec Docker Compose

```bash
docker-compose up --build
```

L'API est accessible sur `http://localhost:8000/docs`

### Ou utiliser l'image Docker Hub directement

```bash
docker pull bilalmdev164/api-rest:latest
```

## Endpoints

| Méthode | Route | Auth | Description |
|---------|-------|------|-------------|
| GET | `/` | Non | Status de l'API |
| POST | `/auth/register` | Non | Créer un compte |
| POST | `/auth/login` | Non | Se connecter |
| GET | `/users/` | Non | Lister les utilisateurs |
| GET | `/users/me` | Oui | Profil connecté |
| GET | `/users/{id}` | Non | Récupérer un utilisateur |
| PUT | `/users/{id}` | Non | Modifier un utilisateur |
| DELETE | `/users/{id}` | Non | Supprimer un utilisateur |

## Ce que j'ai appris

- Structurer une API REST avec séparation des responsabilités
- Implémenter une authentification JWT de bout en bout
- Utiliser un ORM pour interagir avec une base de données relationnelle
- Écrire des tests d'intégration automatisés et isolés
- Containeriser une application avec Docker et Docker Compose
- Mettre en place un pipeline CI/CD avec GitHub Actions
- Déployer une application Python sur le cloud