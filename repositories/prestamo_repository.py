# Se importan las clases necesarias de SQLAlchemy para definir el modelo de datos
from sqlalchemy.orm import Session
from models.prestamo import PrestamoModel

# Se define la clase PrestamoRepository que maneja las operaciones de la base de datos para los préstamos
class PrestamoRepository:
    def __init__(self, db: Session):
        self.db = db
    # Se define el método crear que recibe un objeto prestamo y lo agrega a la base de datos, luego devuelve el prestamo creado
    def crear(self, prestamo: PrestamoModel) -> PrestamoModel:
        self.db.add(prestamo)
        self.db.commit()
        self.db.refresh(prestamo)
        return prestamo
    # Se define el método obtener_por_id que recibe un prestamo_id y devuelve el prestamo correspondiente de la base de datos
    def obtener_por_id(self, prestamo_id: int) -> PrestamoModel:
        return self.db.query(PrestamoModel).filter(PrestamoModel.id == prestamo_id).first()