import bcrypt
#from models.usuario import User

class UserFactory:
    @staticmethod
    def encriptar_contrasena(contrasena):
        return bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt())

    @staticmethod
    def validate_password(contrasena, contrasena_encriptada):
        return bcrypt.checkpw(contrasena.encode("utf-8"), contrasena_encriptada.encode("utf-8"))

