# Se importan las clases necesarias de Pydantic para definir los esquemas de datos que se utilizarán en la API
from pydantic import BaseModel, EmailStr
from typing import Optional

# Se define la clase base para los usuarios, que contiene los campos comunes a todas las operaciones relacionadas con usuarios
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr  # Valida automáticamente que sea un correo válido (ej: usuario@correo.com)
    rol: str = "Lector"

# Se define la clase para la creación de usuarios, que hereda de UsuarioBase y no agrega campos adicionales
class UsuarioCreate(UsuarioBase):
    pass

# Esquema para actualizar usuarios (Campos opcionales)
class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    rol: Optional[str] = None

# Se define la clase para la respuesta de la API al crear o consultar un usuario, que hereda de UsuarioBase y agrega el campo id
class UsuarioResponse(UsuarioBase):
    id: int

    #Se define la configuración de Pydantic para permitir la lectura de atributos desde objetos SQLAlchemy
    class Config:
        from_attributes = True


