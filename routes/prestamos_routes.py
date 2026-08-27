from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.conexion import get_db
from schemas.prestamo_schema import PrestamoCreate, PrestamoResponse
from services.prestamo_service import PrestamoService
from utils.excepciones import RecursoNoEncontradoException, ReglaNegocioException

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("/", response_model=PrestamoResponse, status_code=status.HTTP_201_CREATED)
def registrar_prestamo(data: PrestamoCreate, db: Session = Depends(get_db)):
    service = PrestamoService(db)
    try:
        return service.prestar_libro(data.usuario_id, data.libro_id)
    except RecursoNoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.mensaje)
    except ReglaNegocioException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)