from models.pelicula import Movie
import pyodbc
from dotenv import load_dotenv
import csv
import os
from db.database import DataAcces
load_dotenv()

class MovieDAO:
    #def __init__(self, Temp ):
       # self.temporal = Temp
    @staticmethod
    def insertarPelicula(pelicula:Movie): 
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO peliculas (contenido_id, duracion_minutos) VALUES (?,?) 
                           """, 
                           pelicula.contenido_id, pelicula.duracion_minutos)
            print("La pelicula de duracion: "  ,  str(pelicula.duracion_minutos) , " ha sido insertada exitosamente!.")
            conn.commit()
            conn.close()
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise




    @staticmethod
    def actualizarPelicula(pelicula:Movie):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE peliculas SET duracion_minutos = ? WHERE contenido_id = ?
                           """,
                           pelicula.duracion_minutos, pelicula.contenido_id)
            print("La pelicula de duracion: ", str(pelicula.duracion_minutos), " ha sido actualizada exitosamente!.")
            conn.commit()
            conn.close()
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise

    @staticmethod
    def eliminarPelicula(contenido_id:int):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM peliculas WHERE contenido_id = ?
                           """,
                           contenido_id)
            print("La pelicula con id: ", str(contenido_id), " ha sido eliminada exitosamente!.")
            conn.commit()
            conn.close()
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise


    @staticmethod
    def listarPeliculas():
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM peliculas
                           """)
            peliculas = []
            for row in cursor.fetchall():
                pelicula = Movie(row[0], row[1])
                peliculas.append(pelicula)
            conn.close()
            return peliculas
        except pyodbc.Error as e:
            print("❌ Error al ejeuctar la transacción : descripcion del error : ", e)
            raise
            