from sqlalchemy import Column, Integer, ForeignKey, Date
from database.conexion import Base

class PrestamoModel(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # Relacionamos con las llaves primarias de las tablas usuarios y libros
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    fecha_prestamo = Column(Date, nullable=False)
    fecha_devolucion = Column(Date, nullable=True)