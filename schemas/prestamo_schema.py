#schemas/prestamo_schema.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

# Lo que envía el usuario para solicitar un préstamo
class PrestamoCreate(BaseModel):
    usuario_id: int
    libro_id: int

# Lo que devuelve la API con el préstamo registrado
class PrestamoResponse(BaseModel):
    id: int
    usuario_id: int
    libro_id: int
    fecha_prestamo: date
    fecha_devolucion: Optional[date] = None

    class Config:
        from_attributes = True