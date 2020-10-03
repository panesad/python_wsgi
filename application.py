# -*- coding: utf-8 *-*

import os,sys
from sys import path
sys.path.append('/var/www/sitioweb')
#Ahora se pueden importar los archivos y funciones python directamente sin poner la ruta
from application import connection_db, functions

def application(environ, start_response):
    status = '200 OK'
    # Genero la salida HTML a mostrar al usuario
    peticion = environ['REQUEST_URI']
    if peticion.startswith('/one'):
        output = functions.one()
    elif peticion.startswith('/respuesta'):
        output ='Nada'
    else:
        record = connection_db.select_BBDD_PANES ('tabla_1')
        output = record [0]
    output = bytes(output, encoding='utf-8')
    # Inicio una respuesta al navegador
    response_header = [('Content-type', 'text/html'),('Content-Lenght',str(len(output)))]
    start_response(status, response_header)
    # Retorno el contenido HTML
    return [output]
