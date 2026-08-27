from fastapi import FastAPI
from database.conexion import Base, engine
from routes import libros_routes, usuarios_routes, prestamos_routes

# Esta línea examina todos tus modelos e instruye a MySQL a crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Biblioteca Virtual API",
    description="API RESTful creada con FastAPI, SQLAlchemy y MySQL",
    version="1.0.0"
)

# Registrar routers de cada módulo
app.include_router(libros_routes.router)
app.include_router(usuarios_routes.router)
app.include_router(prestamos_routes.router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "¡Bienvenido a la API de la Biblioteca Virtual!"}