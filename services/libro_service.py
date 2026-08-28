from sqlalchemy.orm import Session
from models.libro import LibroModel
from schemas.libro_schema import LibroCreate
from repositories.libro_repository import LibroRepository
from utils.excepciones import RecursoNoEncontradoException

class LibroService:
    def __init__(self, db: Session):
        self.libro_repo = LibroRepository(db)

    def crear_libro(self, libro_data: LibroCreate) -> LibroModel:
        # Convertimos los datos que vienen del schema Pydantic a un modelo de SQLAlchemy
        nuevo_libro = LibroModel(
            titulo=libro_data.titulo,
            autor=libro_data.autor
        )
        return self.libro_repo.crear(nuevo_libro)

    def obtener_todos(self):
        return self.libro_repo.listar()

    def obtener_por_id(self, libro_id: int) -> LibroModel:
        libro = self.libro_repo.obtener_por_id(libro_id)
        if not libro:
            raise RecursoNoEncontradoException(f"El libro con ID {libro_id} no fue encontrado.")
        return libro