# Se importan las clases necesarias de SQLAlchemy para definir el modelo de datos
from sqlalchemy.orm import Session
from models.libro import LibroModel

# Se define la clase LibroRepository que maneja las operaciones de la base de datos para los libros
class LibroRepository:
    def __init__(self, db: Session):
        self.db = db
    # Se define el método obtener_por_id que recibe un libro_id y devuelve el libro correspondiente de la base de datos
    def obtener_por_id(self, libro_id: int) -> LibroModel:
        return self.db.query(LibroModel).filter(LibroModel.id == libro_id).first()
    # Se define el método listar que devuelve todos los libros de la base de datos
    def listar(self):
        return self.db.query(LibroModel).all()
    # Se define el método crear que recibe un objeto libro y lo agrega a la base de datos, luego devuelve el libro creado
    def crear(self, libro: LibroModel) -> LibroModel:
        self.db.add(libro)
        self.db.commit()
        self.db.refresh(libro)
        return libro
    # Se define el método actualizar que recibe un objeto libro y actualiza sus datos en la base de datos, luego devuelve el libro actualizado
    def actualizar(self, libro: LibroModel) -> LibroModel:
        self.db.commit()
        self.db.refresh(libro)
        return libro
    # Se define el método eliminar que recibe un objeto libro y lo elimina de la base de datos
    def eliminar(self, libro: LibroModel) -> None:
        self.db.delete(libro)
        self.db.commit()