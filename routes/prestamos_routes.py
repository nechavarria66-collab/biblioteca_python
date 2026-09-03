# Se importan las clases necesarias de FastAPI y SQLAlchemy para definir las rutas de la API
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.conexion import get_db
from schemas.prestamo_schema import PrestamoCreate, PrestamoResponse
from services.prestamo_service import PrestamoService
from utils.excepciones import RecursoNoEncontradoException, ReglaNegocioException

# Se crea un enrutador de FastAPI para manejar las rutas relacionadas con los préstamos, con un prefijo "/prestamos" y una etiqueta "Préstamos"
router = APIRouter(prefix="/prestamos", tags=["Préstamos"])
# Se define la ruta POST para registrar un nuevo préstamo, que recibe un objeto PrestamoCreate y devuelve un objeto PrestamoResponse con el préstamo registrado
@router.post("/", response_model=PrestamoResponse, status_code=status.HTTP_201_CREATED)
def registrar_prestamo(data: PrestamoCreate, db: Session = Depends(get_db)):
    service = PrestamoService(db)
    try:
        return service.prestar_libro(data.usuario_id, data.libro_id)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.mensaje)
    except ReglaNegocioException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)