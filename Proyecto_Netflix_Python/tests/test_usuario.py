
from models.usuario import Usuario

def test_usuario_creacion():
    usuario = Usuario("Carlos", "carlos@email.com")
    assert usuario.nombre == "Carlos"
    assert usuario.email == "carlos@email.com"
