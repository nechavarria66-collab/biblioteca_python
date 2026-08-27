from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.conexion import get_db
from schemas.libro_schema import LibroCreate, LibroResponse
from services.libro_service import LibroService
from utils.excepciones import BibliotecaException

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroResponse, status_code=status.HTTP_201_CREATED)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    service = LibroService(db)
    try:
        return service.crear_libro(libro)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)

@router.get("/", response_model=list[LibroResponse])
def listar_libros(db: Session = Depends(get_db)):
    service = LibroService(db)
    return service.obtener_todos()

@router.get("/{libro_id}", response_model=LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    service = LibroService(db)
    try:
        return service.obtener_por_id(libro_id)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.mensaje)