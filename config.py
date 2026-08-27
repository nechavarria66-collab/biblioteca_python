from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Biblioteca Virtual"
    DATABASE_URL: str  # Pydantic buscará esta variable en el archivo .env

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()