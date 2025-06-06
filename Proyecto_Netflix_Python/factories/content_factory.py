from models.contenido import Content
import json
from datetime import datetime   
import bcrypt
#from models.usuario import User

class ContentFactory:
    @staticmethod
    def contenido_factory_from_json(path_json):
        with open(path_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        contenidos = []
        for item in datos:
            fecha = None
            if item.get('fecha_lanzamiento'):
                fecha = datetime.strptime(item['fecha_lanzamiento'], '%Y-%m-%d').date()
            contenido = Content(
                titulo=item['titulo'],
                descripcion=item.get('descripcion'),
                fecha_lanzamiento=fecha,
                tipo_contenido=item['tipo_contenido']
            )
            contenidos.append(contenido)
        return contenidos