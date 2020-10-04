import os,sys
#import fnmatch
from sys import path
sys.path.append('/var/www/sitioweb')
#Ahora se pueden importar los archivos y funciones python directamente sin poner la ruta
from application import functions, two

files = [ ('/one',          'one.html',         'text/html' ),
          ('/scriptOne',    'scriptOne.js',     'application/javascript' ),
          ('/styleOne',     'styleOne.css',     'text/css' ),
          ('/Texto',        'Texto.txt',        'text/plain'),
          ('/pic_demo',     'pic_demo.jpg',     'image/jpeg' ),
          ('/vid_demo',     'vid_demo.mp4',     'video/mp4')
        ]

def application(environ, start_response):
    # Genero la salida HTML a mostrar al usuario
    output = 'No se encuentra'
    status = '404 Not Found'
    response_header = [('Content-type', 'text/html'),('Content-Lenght',str(len(output)))]

    peticion = environ['REQUEST_URI']
    #Archivos
    for path, file, typeFile  in files:
        if peticion.startswith(path):
            record = functions.fileToByteStr(file)
            output = record [0]
            status = '200 OK'
            response_header = [('Content-type', typeFile),('Content-Lenght',str(len(output)))]
    #Funciones
    if peticion.startswith('/two'):
            record = two.gen_html()
            output = record [0]
            status = '200 OK'
            response_header = [('Content-type', 'text/html'),('Content-Lenght',str(len(output)))]
    elif peticion.endswith('/BD'):
            record = functions.select_BBDD ('tabla_1')
            output = record [0]
            status = '200 OK'
            response_header = [('Content-type', 'text/html'),('Content-Lenght',str(len(output)))]
            output = bytes(output, encoding='utf-8')
    start_response(status, response_header)
        # Inicio una respuesta al navegador
    # Retorno el contenido HTML
    return [output]
