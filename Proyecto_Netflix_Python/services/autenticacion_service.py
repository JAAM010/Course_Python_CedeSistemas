
from repositories.usuario_repository import UsuarioRepository

class AutenticacionService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def login(self, email: str, password: str) -> bool:
        usuario = self.repo.obtener_usuario_por_email(email)
        if not usuario:
            print("Usuario no encontrado")
            return False
        # Para este ejemplo, se asume que la contraseña es igual al email invertido
        return password == email[::-1]
