from datetime import date
from sqlalchemy.orm import Session
from models.prestamo import PrestamoModel
from repositories.libro_repository import LibroRepository
from repositories.usuario_repository import UsuarioRepository
from utils.excepciones import RecursoNoEncontradoException, ReglaNegocioException

class PrestamoService:
    def _init_(self, db: Session):
        self.db = db
        self.libro_repo = LibroRepository(db)
        self.usuario_repo = UsuarioRepository(db)

    def prestar_libro(self, usuario_id: int, libro_id: int) -> PrestamoModel:
        # 1. Validar si el usuario existe
        usuario = self.usuario_repo.obtener_por_id(usuario_id)
        if not usuario:
            raise RecursoNoEncontradoException("El usuario especificado no existe.")

        # 2. Validar si el libro existe
        libro = self.libro_repo.obtener_por_id(libro_id)
        if not libro:
            raise RecursoNoEncontradoException("El libro especificado no existe.")

        # 3. Validar si el libro está disponible
        if not libro.disponible:
            raise ReglaNegocioException("El libro ya se encuentra prestado.")

        # 4. Cambiar disponibilidad a False y guardar préstamo
        libro.disponible = False
        self.libro_repo.actualizar(libro)

        nuevo_prestamo = PrestamoModel(
            usuario_id=usuario_id,
            libro_id=libro_id,
            fecha_prestamo=date.today()
        )
        self.db.add(nuevo_prestamo)
        self.db.commit()
        self.db.refresh(nuevo_prestamo)
        return nuevo_prestamo