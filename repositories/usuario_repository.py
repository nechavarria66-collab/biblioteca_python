# Se importan las clases necesarias de SQLAlchemy para definir el modelo de datos
from sqlalchemy.orm import Session
from models.usuario import UsuarioModel

# Se define la clase UsuarioRepository que maneja las operaciones de la base de datos para los usuarios
class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
    # Se define el método obtener_por_id que recibe un usuario_id y devuelve el usuario correspondiente de la base de datos
    def obtener_por_id(self, usuario_id: int) -> UsuarioModel:
        return self.db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()
    # Se define el método obtener_por_email que recibe un email y devuelve el usuario correspondiente de la base de datos
    def obtener_por_email(self, email: str) -> UsuarioModel:
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
    # Se define el método crear que recibe un objeto usuario y lo agrega a la base de datos, luego devuelve el usuario creado
    def crear(self, usuario: UsuarioModel) -> UsuarioModel:
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    # Se define el método listar_todos que devuelve una lista de todos los usuarios registrados en la base de datos
    def listar_todos(self):
        return self.db.query(UsuarioModel).all()
