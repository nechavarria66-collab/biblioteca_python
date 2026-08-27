from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.conexion import get_db
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from services.usuario_service import UsuarioService
from utils.excepciones import BibliotecaException

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    try:
        return service.registrar_usuario(usuario)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    try:
        return service.obtener_por_id(usuario_id)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.mensaje)
