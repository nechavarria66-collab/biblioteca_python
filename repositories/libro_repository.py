from sqlalchemy.orm import Session
from models.libro import LibroModel

class LibroRepository:
    def __init__(self, db: Session):
        self.db = db

    def obtener_por_id(self, libro_id: int) -> LibroModel:
        return self.db.query(LibroModel).filter(LibroModel.id == libro_id).first()

    def listar(self):
        return self.db.query(LibroModel).all()

    def crear(self, libro: LibroModel) -> LibroModel:
        self.db.add(libro)
        self.db.commit()
        self.db.refresh(libro)
        return libro

    def actualizar(self, libro: LibroModel) -> LibroModel:
        self.db.commit()
        self.db.refresh(libro)
        return libro