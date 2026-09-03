# Se importan las clases necesarias de FastAPI y SQLAlchemy para definir las rutas de la API
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.conexion import get_db
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from services.usuario_service import UsuarioService
from utils.excepciones import BibliotecaException

# Se crea un enrutador de FastAPI para manejar las rutas relacionadas con los usuarios, con un prefijo "/usuarios" y una etiqueta "Usuarios"
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Se define la ruta POST para registrar un nuevo usuario, que recibe un objeto UsuarioCreate y devuelve un objeto UsuarioResponse con el usuario registrado
@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    try:
        return service.registrar_usuario(usuario)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)
    
# Se define la ruta GET para obtener un usuario por su ID, que recibe un usuario_id y devuelve un objeto UsuarioResponse con el usuario correspondiente
@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    try:
        return service.obtener_por_id(usuario_id)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.mensaje)
