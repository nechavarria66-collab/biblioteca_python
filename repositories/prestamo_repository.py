
from sqlalchemy.orm import Session
from models.prestamo import PrestamoModel

class PrestamoRepository:
    def _init_(self, db: Session):
        self.db = db

    def crear(self, prestamo: PrestamoModel) -> PrestamoModel:
        self.db.add(prestamo)
        self.db.commit()
        self.db.refresh(prestamo)
        return prestamo

    def obtener_por_id(self, prestamo_id: int) -> PrestamoModel:
        return self.db.query(PrestamoModel).filter(PrestamoModel.id == prestamo_id).first()