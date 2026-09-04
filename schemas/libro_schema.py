# Se importan las clases necesarias de Pydantic para definir los esquemas de datos que se utilizarán en la API
from pydantic import BaseModel
from typing import Optional
# Esquema base con los atributos comunes
class LibroBase(BaseModel):
    titulo: str
    autor: str
# Esquema para cuando el usuario envíe datos para CREAR un libro
class LibroCreate(LibroBase):
    pass
# Esquema para cuando el usuario envíe datos para ACTUALIZAR un libro (Campos opcionales)
class LibroUpdate(BaseModel):
    titulo: Optional[str] = None
    autor: Optional[str] = None
    disponible: Optional[bool] = None
# Esquema para cuando la API le RESPONDA al usuario (incluye id y disponibilidad)
class LibroResponse(LibroBase):
    id: int
    disponible: bool
    # Se define la configuración de Pydantic para permitir la lectura de atributos desde objetos SQLAlchemy
    class Config:
        from_attributes = True  # Permite que Pydantic lea datos directamente de SQLAlchemy

        