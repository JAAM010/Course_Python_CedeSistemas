from models.usuario import User
from factories.user_factory import UserFactory
import pyodbc
from dotenv import load_dotenv
import csv
import os
from datetime import datetime
from db.database import DataAcces
load_dotenv()


class UserDAO:
    #def __init__(self, Temp ):
       # self.temporal = Temp
    @staticmethod
    def add(usuario:User): 
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    INSERT INTO usuarios (nombre, email, contrasena)
                    VALUES (?, ?, ?)
                    """,
                    usuario.nombre, usuario.email, UserFactory.encriptar_contrasena(usuario.contrasena)  
                )
            print("El usuario : "  ,  usuario.nombre , " ha sido actualizado exitosamente!.")
            conn.commit()
            conn.close()
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise


    @staticmethod
    def update(usuario:User):
        try:
            #print ("idUsuario : " + str(usuario.id))
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    UPDATE usuarios SET nombre = ?, email = ?, contrasena = ? WHERE id = ?
                    """,
                    usuario.nombre, usuario.email, UserFactory.encriptar_contrasena(usuario.contrasena), usuario.id
                )
            conn.commit()
            conn.close()
            print("El usuario : " , str(usuario.id) , " " ,  usuario.nombre , " ha sido actualizado exitosamente!.")
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise




    @staticmethod
    def eliminarUsuario(id:int):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    DELETE FROM usuarios WHERE id = ?
                    """,
                    id
                )
            conn.commit()
            conn.close()
            print("El usuario : " , str(id) , " ha sido eliminado exitosamente!.")
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise

    
    @staticmethod
    def autenticarUsuario(email, contrasena):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    Select * FROM usuarios WHERE email = ? 
                    """,
                    email
                )
            resultados = cursor.fetchall()    
            conn.close()
            return [
                User(id=row[0], nombre=row[1], email=row[2], contrasena=row[3])
                for row in resultados]
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise




    @staticmethod
    def listarUsuarios():
        try:
            #print ("Entro Bien ")
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, email, contrasena FROM dbo.Usuarios")
            rows = cursor.fetchall()
            conn.close()
            return [
                User(id=row[0], nombre=row[1], email=row[2], contrasena=row[3])
                for row in rows]
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise



    #@staticmethod
    def cargarUsuarios_from_csv(path_csv):
        usuarios = []
        with open(path_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                usuario = User(
                    id=0,
                    nombre=row['nombre'],
                    email=row['email'],
                    contrasena=row['contrasena']
                )
                usuarios.append(usuario)
        return usuarios


    # def cargarUsuarios_from_json(path_json):
    # with open(path_json, 'r', encoding='utf-8') as f:
    #     datos = json.load(f)
    
    # contenidos = []
    # for item in datos:
    #     fecha = None
    #     if item.get('fecha_lanzamiento'):
    #         fecha = datetime.strptime(item['fecha_lanzamiento'], '%Y-%m-%d').date()
    #     contenido = Contenido(
    #         titulo=item['titulo'],
    #         descripcion=item.get('descripcion'),
    #         fecha_lanzamiento=fecha,
    #         tipo_contenido=item['tipo_contenido']
    #     )
    #     contenidos.append(contenido)
    # return contenidos


    