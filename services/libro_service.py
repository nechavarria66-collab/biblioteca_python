# Se importan las clases necesarias de SQLAlchemy y los modelos, esquemas y repositorios relacionados con los libros
from sqlalchemy.orm import Session
from models.libro import LibroModel
from schemas.libro_schema import LibroCreate
from repositories.libro_repository import LibroRepository
from utils.excepciones import RecursoNoEncontradoException

# Se define la clase de servicio para los libros, que contiene la lógica de negocio relacionada con los libros
class LibroService:
    def __init__(self, db: Session):
        self.libro_repo = LibroRepository(db)

    # Se define el método para crear un nuevo libro, que recibe los datos del libro en formato de esquema Pydantic y devuelve el modelo de SQLAlchemy correspondiente
    def crear_libro(self, libro_data: LibroCreate) -> LibroModel:
        # Convertimos los datos que vienen del schema Pydantic a un modelo de SQLAlchemy
        nuevo_libro = LibroModel(
            titulo=libro_data.titulo,
            autor=libro_data.autor
        )
        return self.libro_repo.crear(nuevo_libro)

    # Se define el método para obtener todos los libros, que devuelve una lista de modelos de SQLAlchemy
    def obtener_todos(self):
        return self.libro_repo.listar()

    # Se define el método para obtener un libro por su ID, que recibe el ID del libro y devuelve el modelo de SQLAlchemy correspondiente
    def obtener_por_id(self, libro_id: int) -> LibroModel:
        libro = self.libro_repo.obtener_por_id(libro_id)
        if not libro:
            raise RecursoNoEncontradoException(f"El libro con ID {libro_id} no fue encontrado.")
        return libro