class BibliotecaException(Exception):
    """Excepción base del sistema"""
    def _init_(self, mensaje: str):
        self.mensaje = mensaje

class RecursoNoEncontradoException(BibliotecaException):
    """Se lanza cuando un libro o usuario no existe"""
    pass

class ReglaNegocioException(BibliotecaException):
    """Se lanza cuando se violan reglas (ej: prestar un libro no disponible)"""
    pass