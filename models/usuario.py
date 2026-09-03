# Se importan las clases necesarias de SQLAlchemy para definir el modelo de datos
from sqlalchemy import Column, Integer, String
from database.conexion import Base

# Se define la clase UsuarioModel que hereda de Base, representando la tabla "usuarios" en la base de datos
class UsuarioModel(Base):
    __tablename__ = "usuarios"

    # Se definen las columnas de la tabla "usuarios" con sus respectivos tipos de datos y restricciones
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)

    # Email es único para evitar duplicados en la base de datos
    email = Column(String(150), unique=True, index=True, nullable=False)
    rol = Column(String(50), default="Lector")  # Puede ser "Lector" o "Bibliotecario"