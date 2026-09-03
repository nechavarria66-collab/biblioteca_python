# Se importan las clases necesarias de FastAPI y SQLAlchemy para definir las rutas de la API
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.conexion import get_db
from schemas.libro_schema import LibroCreate, LibroResponse
from services.libro_service import LibroService
from utils.excepciones import BibliotecaException

# Se crea un enrutador de FastAPI para manejar las rutas relacionadas con los libros, con un prefijo "/libros" y una etiqueta "Libros"
router = APIRouter(prefix="/libros", tags=["Libros"])

# Se define la ruta POST para crear un nuevo libro, que recibe un objeto LibroCreate y devuelve un objeto LibroResponse con el libro creado
@router.post("/", response_model=LibroResponse, status_code=status.HTTP_201_CREATED)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    service = LibroService(db)
    try:
        return service.crear_libro(libro)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.mensaje)
# Se define la ruta GET para listar todos los libros, que devuelve una lista de objetos LibroResponse
@router.get("/", response_model=list[LibroResponse])
def listar_libros(db: Session = Depends(get_db)):
    service = LibroService(db)
    return service.obtener_todos()
# Se define la ruta GET para obtener un libro por su ID, que recibe un libro_id y devuelve un objeto LibroResponse con el libro correspondiente
@router.get("/{libro_id}", response_model=LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    service = LibroService(db)
    try:
        return service.obtener_por_id(libro_id)
    except BibliotecaException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.mensaje)