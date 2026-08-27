from sqlalchemy.orm import Session
from models.usuario import UsuarioModel
from schemas.usuario_schema import UsuarioCreate
from repositories.usuario_repository import UsuarioRepository
from utils.excepciones import ReglaNegocioException, RecursoNoEncontradoException

class UsuarioService:
    def _init_(self, db: Session):
        self.usuario_repo = UsuarioRepository(db)

    def registrar_usuario(self, usuario_data: UsuarioCreate) -> UsuarioModel:
        # Validar si ya existe un usuario con el mismo email
        existente = self.usuario_repo.obtener_por_email(usuario_data.email)
        if existente:
            raise ReglaNegocioException("Ya existe un usuario registrado con este correo electrónico.")

        nuevo_usuario = UsuarioModel(
            nombre=usuario_data.nombre,
            email=usuario_data.email,
            rol=usuario_data.rol
        )
        return self.usuario_repo.crear(nuevo_usuario)

    def obtener_por_id(self, usuario_id: int) -> UsuarioModel:
        usuario = self.usuario_repo.obtener_por_id(usuario_id)
        if not usuario:
            raise RecursoNoEncontradoException(f"El usuario con ID {usuario_id} no fue encontrado.")
        return usuario