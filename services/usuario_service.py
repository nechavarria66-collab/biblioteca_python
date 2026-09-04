# Se importan las clases necesarias de SQLAlchemy, los modelos y esquemas relacionados con los usuarios, el repositorio de usuarios y las excepciones personalizadas
from sqlalchemy.orm import Session
from models.usuario import UsuarioModel
from schemas.usuario_schema import UsuarioCreate, UsuarioUpdate
from repositories.usuario_repository import UsuarioRepository
from utils.excepciones import ReglaNegocioException, RecursoNoEncontradoException

# Se define la clase de servicio para los usuarios, que contiene la lógica de negocio relacionada con los usuarios
class UsuarioService:
    def __init__(self, db: Session):
        self.usuario_repo = UsuarioRepository(db)

    # Se define el método para registrar un nuevo usuario, que recibe los datos del usuario en formato de esquema Pydantic y devuelve el modelo de SQLAlchemy correspondiente
    def registrar_usuario(self, usuario_data: UsuarioCreate) -> UsuarioModel:
        # Validar si ya existe un usuario con el mismo email
        existente = self.usuario_repo.obtener_por_email(usuario_data.email)
        if existente:
            raise ReglaNegocioException("Ya existe un usuario registrado con este correo electrónico.")

        # Se crea un nuevo registro de usuario con los datos proporcionados y se guarda en la base de datos
        nuevo_usuario = UsuarioModel(
            nombre=usuario_data.nombre,
            email=usuario_data.email,
            rol=usuario_data.rol
        )
        return self.usuario_repo.crear(nuevo_usuario)

    # Se define el método para obtener un usuario por su ID, que recibe el ID del usuario y devuelve el modelo de SQLAlchemy correspondiente
    def obtener_por_id(self, usuario_id: int) -> UsuarioModel:
        usuario = self.usuario_repo.obtener_por_id(usuario_id)
        if not usuario:
            raise RecursoNoEncontradoException(f"El usuario con ID {usuario_id} no fue encontrado.")
        return usuario

    # Se define el método para obtener todos los usuarios, que devuelve una lista de modelos de SQLAlchemy correspondientes a todos los usuarios registrados
    def obtener_todos(self):
        return self.usuario_repo.listar_todos()

    def actualizar_usuario(self, usuario_id: int, usuario_data: UsuarioUpdate) -> UsuarioModel:
        # 1. Verificar si el usuario existe
        usuario = self.usuario_repo.obtener_por_id(usuario_id)
        if not usuario:
            raise RecursoNoEncontradoException(f"El usuario con ID {usuario_id} no fue encontrado.")

         # 2. Si se desea actualizar el email, validar que no esté duplicado en otro usuario
        if usuario_data.email and usuario_data.email != usuario.email:
            existente = self.usuario_repo.obtener_por_email(usuario_data.email)
            if existente:
                raise ReglaNegocioException("Ya existe otro usuario registrado con este correo electrónico.")
            usuario.email = usuario_data.email

        # 3. Actualizar los demás campos si vienen en la petición
        if usuario_data.nombre is not None:
            usuario.nombre = usuario_data.nombre
        if usuario_data.rol is not None:
            usuario.rol = usuario_data.rol

        # 4. Guardar cambios en la base de datos MySQL
        return self.usuario_repo.actualizar(usuario)

    # Se define el método para eliminar un usuario por su ID, que recibe el ID del usuario y elimina el registro correspondiente de la base de datos
    def eliminar_usuario(self, usuario_id: int) -> None:
        # 1. Verificar si el usuario existe en la base de datos MySQL
        usuario = self.usuario_repo.obtener_por_id(usuario_id)
        if not usuario:
            raise RecursoNoEncontradoException(f"El usuario con ID {usuario_id} no fue encontrado.")

        # 2. Eliminar el usuario de la base de datos MySQL
        self.usuario_repo.eliminar(usuario)