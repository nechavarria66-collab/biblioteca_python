from sqlalchemy.orm import Session
from models.usuario import UsuarioModel

class UsuarioRepository:
    def _init_(self, db: Session):
        self.db = db

    def obtener_por_id(self, usuario_id: int) -> UsuarioModel:
        return self.db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()

    def obtener_por_email(self, email: str) -> UsuarioModel:
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

    def crear(self, usuario: UsuarioModel) -> UsuarioModel:
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario