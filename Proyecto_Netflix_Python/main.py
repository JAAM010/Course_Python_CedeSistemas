from models.usuario import User
from models.contenido import Content
from models.pelicula import Movie 
from models.serie import Show
from  models.visualizacion import ViewRecord 
from repositories.usuario_repository import UserDAO
from repositories.contenido_repository import ContentDAO
from repositories.pelicula_repository import MovieDAO 
from repositories.serie_repository import ShowDAO
from repositories.visualizacion_repository import ViewDAO
from factories.user_factory import UserFactory
from factories.content_factory import ContentFactory






##Insertar un usuario
UserDAO.add(User("Roland", "elroland@empresas.com.com.co", "contraseña123"))

###Actualizacar usuario
UserDAO.update(User("Rodrigo Salazar Alzate", "rodrigo_edicioncorreo@empresas.com.co", "contraseña123",21))
    
##Un factory de suaurio para validar la contraseña o autenticarse
es_correcta = UserFactory.validate_password("contraseña123","$2b$12$Mu9apOTSdbw83I4VxyEKCe02zh.Rz8yqTnTvznjDycI7xcdv9Kv0a")
if es_correcta:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")    


###Autenticar usuario usando una funcion que verifica si la contraseña es valida
listaUser= UserDAO.autenticarUsuario("rolandneew@empresas.com.com.co","contraseña123")
print("id usuario:", listaUser[0].id, ", Nombre usuario:", listaUser[0].nombre, ", Email usuario:", listaUser[0].email, ", Password usuario:", listaUser[0].contrasena) 
if listaUser.count==0:
    print("No existe el usuario")   
if len(listaUser)> 1:
    print("Se encontraron varios usuarios con el mismo correo electrónico.")    
else:
    esCorrecta= UserFactory.validate_password("contraseña123", listaUser[0].contrasena)
    if esCorrecta:
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")    


print("No existe el usuario")
for usuario in listaUser:
    print ("id usuario:" , usuario.id, ", Nombre usuario:", usuario.nombre, ", Email usuario:", usuario.email, ", Password usuario:", usuario.contrasena)


##Listar e imprimir la lista de usuarios
UserDAO.listarUsuarios()
for usuario in UserDAO.listarUsuarios():
  print ("id usuario:" , usuario.id, ",Nombre usuario:", usuario.nombre, ",Email usuario:", usuario.email, ",Password usuario:", usuario.contrasena) 


###lee el archivo de csv de usuarios y los inserta en la base de datos
lstusuarios =UserDAO.cargarUsuarios_from_csv("usuarios.csv")
for usuario in lstusuarios:
    print (",Nombre usuario:", usuario.nombre, ",Email usuario:", usuario.email, ",Password usuario:", usuario.contrasena) 
    UserDAO.add(usuario)



######################## COntenidos ##########################################
contenidos = ContentFactory.contenido_factory_from_json('contenidos.json')
for contenido in contenidos:
    ContentDAO.insertarContenido(contenido)   
print("Contenidos insertados desde JSON.")

contenidos = ContentDAO.listarContenidos()    
for contenido in contenidos:
    print("Título:", contenido.titulo)
    print("Descripción:", contenido.descripcion)
    print("Fecha de lanzamiento:", contenido.fecha_lanzamiento)
    print("Tipo de contenido:", contenido.tipo_contenido)
    print() 

ContentDAO.insertarContenido(Content("Desde mi Cielo","Pelicula cristiana", "2007-01-23","Pelicula"))
ContentDAO.actualizarContenido(Content("Desde mi Cielo", "Pelicula familiar", "2001-01-01", "Pelicula", 48) )
ContentDAO.eliminarContenido(48)

######################## Peliculas ##########################################
MovieDAO.insertarPelicula(Movie(11, 185))
MovieDAO.actualizarPelicula(Movie(11, 100))
MovieDAO.listarPeliculas()
for pelicula in MovieDAO.listarPeliculas():
    print("Contenido ID:", pelicula.contenido_id)
    print("Duración en minutos:", pelicula.duracion_minutos)
    print() 
MovieDAO.eliminarPelicula(11)



######################## Series ##########################################
ShowDAO.insertarSerie(Show(11, 10))    
ShowDAO.actualizarSerie(Show(11, 5))
series= ShowDAO.listarSeries()
for serie in series:
    print("Contenido ID:", serie.contenido_id)
    print("Cantidad de temporadas:", serie.cantidad_temporadas)
    print() 
ShowDAO.eliminarSerie(11)  



######################## Visulizacion ##########################################
ViewDAO.insertarVisualizacion(ViewRecord(1, 1, "2024-04-01") ) 
ViewDAO.listarVisualizaciones()
for visualizacion in ViewDAO.listarVisualizaciones():
    print("Usuario ID:", visualizacion.usuario_id)
    print("Contenido ID:", visualizacion.contenido_id)
    print("Fecha de visualización:", visualizacion.fecha_visualizacion)
    print() 
ViewDAO.eliminarVisualizacion(5)
ViewDAO.actualizarVisualizacion(ViewRecord(2, 2, "2025-04-01", 7 ))