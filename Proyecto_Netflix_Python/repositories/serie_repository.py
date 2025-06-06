import pyodbc
from dotenv import load_dotenv
import csv
import os
from db.database import DataAcces
from models.serie import Show


class ShowDAO :
    staticmethod
    def insertarSerie(serie: Show):
        try:
            conn = DataAcces.get_connection()   
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO Series (contenido_id, cantidad_temporadas) VALUES (?, ?)
                           """, 
                            serie.contenido_id, serie.cantidad_temporadas)
            conn.commit()
            conn.close()
            print("Serie insertada correctamente.")
        except Exception as e:
            print("Error al insertar la serie:", e)

    staticmethod
    def actualizarSerie(serie: Show):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE Series SET cantidad_temporadas = ? WHERE contenido_id = ?
                           """,
                            serie.cantidad_temporadas, serie.contenido_id)
            conn.commit()
            conn.close()
            print("Serie actualizada correctamente.")
        except Exception as e:
            print("Error al actualizar la serie:", e)   


    staticmethod
    def eliminarSerie(contenido_id: int):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM Series WHERE contenido_id = ?
                           """,
                            contenido_id)
            conn.commit()
            conn.close()
            print("Serie eliminada correctamente.")
        except Exception as e:
            print("Error al eliminar la serie:", e) 
    
    staticmethod
    def  listarSeries():
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM Series""")
            series = []
            for row in cursor.fetchall():
                serie = Show(row[0], row[1])
                series.append(serie)
            conn.close()
            return series
        except Exception as e:
            print("Error al listar las series:", e) 