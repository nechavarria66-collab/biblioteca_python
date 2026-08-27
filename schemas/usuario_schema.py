#schemas/usuario_schema.py
from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr  # Valida automáticamente que sea un correo válido (ej: usuario@correo.com)
    rol: str = "Lector"

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True