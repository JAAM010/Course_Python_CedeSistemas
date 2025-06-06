from models.contenido import Content
#from factories.user_factory import UserFactory
import pyodbc
from dotenv import load_dotenv
import csv
import os
from datetime import datetime
from db.database import DataAcces
load_dotenv()


class ContentDAO:
    #def __init__(self, Temp ):
       # self.temporal = Temp
    @staticmethod
    def insertarContenido(contenido:Content): 
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    INSERT INTO contenidos ( titulo, descripcion, fecha_lanzamiento, tipo_contenido )
                    VALUES (?, ?, ?, ?)
                    """,
                    contenido.titulo, contenido.descripcion, contenido.fecha_lanzamiento , contenido.tipo_contenido
                )
            print("El contenido : " ,  contenido.titulo , " ha sido actualizado exitosamente!.")
            conn.commit()
            conn.close()
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise


    @staticmethod
    def actualizarContenido(contenido:Content):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    UPDATE Contenidos  SET titulo = ?, descripcion = ?, fecha_lanzamiento = ?, tipo_contenido=? WHERE id = ?
                    """,
                    contenido.titulo, contenido.descripcion, contenido.fecha_lanzamiento , contenido.tipo_contenido, contenido.id
                )
            conn.commit()
            conn.close()
            print("El Contenido : " , str(contenido.id) , " " ,  contenido.titulo , " ha sido actualizado exitosamente!.")
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise




    @staticmethod
    def eliminarContenido(id:int):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                    """
                    DELETE FROM contenidos WHERE id = ?
                    """,
                    id
                )
            conn.commit()
            conn.close()
            print("El Contendio : " , str(id) , " ha sido eliminado exitosamente!.")
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise

    


    @staticmethod
    def listarContenidos():
        try:
            #print ("Entro Bien ")
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, titulo, descripcion, fecha_lanzamiento, tipo_contenido FROM dbo.contenidos")
            rows = cursor.fetchall()
            conn.close()
            return [
                Content(id=row[0], titulo=row[1], descripcion=row[2], fecha_lanzamiento=row[3], tipo_contenido=row[4])
                for row in rows]
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise
