#Ahora los schemas: libro_schema.py
from pydantic import BaseModel

# Esquema base con los atributos comunes
class LibroBase(BaseModel):
    titulo: str
    autor: str

# Esquema para cuando el usuario envíe datos para CREAR un libro
class LibroCreate(LibroBase):
    pass

# Esquema para cuando la API le RESPONDA al usuario (incluye id y disponibilidad)
class LibroResponse(LibroBase):
    id: int
    disponible: bool

    class Config:
        from_attributes = True  # Permite que Pydantic lea datos directamente de SQLAlchemy