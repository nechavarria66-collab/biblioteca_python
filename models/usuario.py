from sqlalchemy import Column, Integer, String
from database.conexion import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    # email es único para evitar duplicados en la base de datos
    email = Column(String(150), unique=True, index=True, nullable=False)
    rol = Column(String(50), default="Lector")  # Puede ser "Lector" o "Bibliotecario"