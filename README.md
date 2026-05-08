# API REST — FastAPI + PostgreSQL + JWT

Une API REST complète construite avec FastAPI, PostgreSQL et une authentification JWT. Projet réalisé en autonomie pour démontrer mes compétences en développement backend.

## Stack technique

- **Python 3.12** + **FastAPI** — framework web
- **PostgreSQL** — base de données relationnelle
- **SQLAlchemy** — ORM pour interagir avec la BDD
- **JWT** — authentification stateless
- **bcrypt** — hashing des mots de passe
- **Pytest** — tests d'intégration automatisés
- **Render** — déploiement cloud

## Fonctionnalités

- CRUD complet sur les utilisateurs
- Inscription et connexion avec JWT
- Routes protégées par token
- Documentation interactive auto-générée (Swagger)
- 5 tests d'intégration automatisés

## Demo

API disponible en ligne : [https://api-rest-4j5w.onrender.com/docs](https://api-rest-4j5w.onrender.com/docs)

## Lancer le projet en local

### Prérequis
- Python 3.12+
- PostgreSQL

### Installation

```bash
# Cloner le repo
git clone https://github.com/ton-username/api-rest.git
cd api-rest

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration

Crée un fichier `.env` à la racine :

```
DATABASE_URL=postgresql://apiuser:apipassword@localhost:5432/apidb
SECRET_KEY=remplace_par_ta_cle_secrete
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
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
- Déployer une application Python sur le cloud