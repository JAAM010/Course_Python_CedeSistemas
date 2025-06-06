import pyodbc
from dotenv import load_dotenv
import csv
import os
from db.database import DataAcces
from models.visualizacion import ViewRecord

class ViewDAO :
    staticmethod
    def insertarVisualizacion(visualizacion: ViewRecord):
        try:
            conn = DataAcces.get_connection()   
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO Visualizaciones (usuario_id, contenido_id, fecha_visualizacion) VALUES (?, ?, ?)
                           """, 
                            visualizacion.usuario_id, visualizacion.contenido_id, visualizacion.fecha_visualizacion)
            conn.commit()
            conn.close()
            print("Visualizacion insertada correctamente.")
        except Exception as e:
            print("Error al insertar la visualizacion:", e)


    staticmethod
    def actualizarVisualizacion(visualizacion: ViewRecord):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE Visualizaciones SET usuario_id= ?, contenido_id= ?, fecha_visualizacion = ?
                            WHERE  id=?
                           """,
                            visualizacion.usuario_id, visualizacion.contenido_id, visualizacion.fecha_visualizacion, 
                             visualizacion.id)   
            conn.commit()
            conn.close()
            print("Visualizacion actualizada correctamente.")
        except Exception as e:
            print("Error al actualizar la visualizacion:", e)   


    staticmethod
    def eliminarVisualizacion(id: int):
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM Visualizaciones WHERE id = ?
                           """,
                            id)
            conn.commit()
            conn.close()
            print("Visualizacion eliminada correctamente.")
        except Exception as e:
            print("Error al eliminar la visualizacion:", e) 
    
    staticmethod
    def  listarVisualizaciones():
        try:
            conn = DataAcces.get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM Visualizaciones""")
            visualizaciones = []
            for row in cursor.fetchall():
                visualizacion = ViewRecord(row[0], row[1], row[2])
                visualizaciones.append(visualizacion)
            conn.close()
            return visualizaciones
        except Exception as e:
            print("Error al listar las visualizaciones:", e)    