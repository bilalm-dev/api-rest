from pydantic import BaseModel, EmailStr
from datetime import datetime

# Ce que l'API reçoit pour créer un user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Ce que l'API renvoie (jamais le mot de passe)
class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True