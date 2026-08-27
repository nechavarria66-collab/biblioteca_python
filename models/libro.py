from sqlalchemy import Column, Integer, String, Boolean
from database.conexion import Base

class LibroModel(Base):
    __tablename__ = "libros"

    # Definimos las columnas de la tabla 'libros' en MySQL
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    disponible = Column(Boolean, default=True)