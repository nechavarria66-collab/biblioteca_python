# Se importa la clase BaseSettings de pydantic_settings para manejar la configuración de la aplicación
from pydantic_settings import BaseSettings

# Se define la clase Settings que hereda de BaseSettings y contiene las variables de configuración de la aplicación
class Settings(BaseSettings):
    PROJECT_NAME: str = "Biblioteca Virtual"
    DATABASE_URL: str  # Pydantic buscará esta variable en el archivo .env

    # Se define la clase Config dentro de Settings para especificar el archivo .env y su codificación
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Se crea una instancia de la clase Settings para que pueda ser utilizada en otras partes de la aplicación
settings = Settings()