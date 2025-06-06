import pyodbc
from dotenv import load_dotenv
import os



load_dotenv()

class DataAcces :
    # def __init__(self, temporal):
    #     self.temporal = temporal

    @staticmethod
    def get_connection():
        try:
            server = os.getenv('SERVER')
            database = os.getenv('DATABASE')
            username = os.getenv('USERNAME')
            password = os.getenv('PASSWORD')
            driver = '{ODBC Driver 17 for SQL Server}'


            conn_str = f'''
                DRIVER={driver};
                SERVER={server};
                DATABASE={database};
                Trusted_Connection=yes;
            ''' 
            #print(conn_str )
            conn = pyodbc.connect(conn_str)
            return conn
        except pyodbc.Error as e:
            print("❌ Error al conectar a la base de datos: descripcion del error : ", e)
            raise