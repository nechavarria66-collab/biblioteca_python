# Se definen las excepciones personalizadas para el sistema de biblioteca, que heredan de la clase base BibliotecaException
class BibliotecaException(Exception):
    """Excepción base del sistema"""
    def _init_(self, mensaje: str):
        self.mensaje = mensaje

# Se define la excepción personalizada para cuando un recurso (libro o usuario) no se encuentra en la base de datos
class RecursoNoEncontradoException(BibliotecaException):
    """Se lanza cuando un libro o usuario no existe"""
    pass

# Se define la excepción personalizada para cuando se violan reglas de negocio (por ejemplo, intentar prestar un libro que no está disponible)
class ReglaNegocioException(BibliotecaException):
    """Se lanza cuando se violan reglas (ej: prestar un libro no disponible)"""
    pass