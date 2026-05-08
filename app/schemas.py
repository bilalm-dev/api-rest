from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

# Ce que l'API reçoit pour créer un user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Ce que l'API renvoie (jamais le mot de passe)
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    created_at: datetime