from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import users, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API REST",
    description="Une API REST complète avec authentification JWT construite avec FastAPI et PostgreSQL.",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/", tags=["root"])
def root():
    return {"message": "API opérationnelle"}