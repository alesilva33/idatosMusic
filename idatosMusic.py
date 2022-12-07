import csv
import numpy as np
import pandas as pd
from manejoDeGeneros import obtenerGenerosDeCancion

TRACKS_FILEPATH = 'Datasets/tracks_features.csv'
INDEX_ID_CANCIONES = 0  # TODO: AJUSTAR CON DATO DEL DATASET EFECTIVO
INDEX_NOMBRE_CANCIONES = 1  # TODO: AJUSTAR CON DATO DEL DATASET EFECTIVO
INDEX_NOMBRE_ARTISTAS = 4   # TODO: AJUSTAR CON DATO DEL DATASET EFECTIVO

def leerDelCsv(indexDesde):
    with open(TRACKS_FILEPATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        ret = []
        for row in csv_reader:
            if line_count >= indexDesde:
                aux = []
                aux.append(row[INDEX_ID_CANCIONES])
                aux.append(row[INDEX_NOMBRE_CANCIONES])
                aux.append(row[INDEX_NOMBRE_ARTISTAS])
                ret.append(aux)
            if indexDesde + 4 == line_count:
                break
            line_count += 1
    return ret

def mensajesBase():
    print(' Seleccione 5 canciones, aca tenes 5 para elegir.\n\n - i {id} --> Comando para seleccionar una cancion. {id} es el identificador mostrado en las canciones expuestas.\n - r      --> Comando para desplegar 5 canciones mas.\n\n')
    print('========== CANCIONES ==========')
    print('---------- ID ---------- NOMBRE ---------- ARTISTAS ----------')

def manejoDeComandos(current, elegidos):
    for cur in current:
        print('---------- ' + str(cur[0]) + ' ---------- ' + str(cur[1]) + ' ---------- ' + str(cur[2]) + ' ---------- ')
    comandoIncorrecto = True
    while (comandoIncorrecto):
        comando = input("Comando: ")
        if str(comando) != 'r' and (not str(comando).startswith('i ')):
            print('Comando incorrecto!\n')
        else:
            if str(comando) == 'r':
                return ([], elegidos, True)
            else:
                elem = str(comando).rsplit('i ', 1)[1]
                found = False
                count = 0
                for cur in current:
                    if (cur[0] == elem):
                        found = True
                        break
                    else:
                        count += 1
                if found:
                    elegidos.append(current[count])
                    current.pop(count)
                    return (current, elegidos, False)
                else:
                    print('El Id elegido no esta presente entre los mostrados.\n')
    
def generosDeCancionesElegidas(elegidos):
    ret = []
    for elem in elegidos:
        # TODO CAMBIAR EL PARAMETROS PASADO EN FUNCIOIN obtenerGenerosDeCancion POR LOS VALORES DE LA CANCION QUE SE ESTA RECORRIENDO
        elem.append(obtenerGenerosDeCancion({'danceability': 0.47, 'acoustucness': 0.0261, 'energy': 0.978, 'key': 7, 'instrumentalness': 1.09e-05, 'valence': 0.35600000000000004, 'tempo': 117.906}))
        ret.append(elem)
    return ret

def recomendarCancion(elegidosConGeneros,nivelDeDificultad):
    print('TODO: FALTA IMPLEMENTAR')
def observarDatosIngresados(elegidosConGeneros,nivelDeDificultad):
    print('TODO: FALTA IMPLEMENTAR')
def verGenerosDeCancion():
    print('TODO: FALTA IMPLEMENTAR')


# MAIN

print('==================== BIENVENIDO A IDatos Music ====================')
index = 1
elegidos = []
elementoElegido = False
while (len(elegidos) < 5):
    mensajesBase()
    if not elementoElegido:
        current = leerDelCsv(index)
        index += 5
        (current, elegidos, recargar) = manejoDeComandos(current, elegidos)
    else:
        (current, elegidos, recargar) = manejoDeComandos(current, elegidos)
    elementoElegido = not recargar

elegidosConGeneros = generosDeCancionesElegidas(elegidos)

print('Ya se han obtenido las 5 canciones de su preferencia. Ahora debe escoger el nivel de dificultad deseado para las canciones a ser recomendadas:\n')
print('==================== 1 --> Novice')
print('==================== 2 --> Intermediate\n')

nivelDeDificultad = ''
comandoIncorrecto = True
while (comandoIncorrecto):
    comando = input("Comando: ")
    if (str(comando) == '1' or str(comando) == '2'):
        comandoIncorrecto = False
        if (str(comando) == '1'):
            nivelDeDificultad = 'novice'
        else:
            nivelDeDificultad = 'intermediate'
    else:
        print('Comando incorrecto!\n')
print('\nYa a terminado el seteo inicial de datos.\n\n')

nosVimo = False
while(not nosVimo):
    print("A conitnuacion cuenta con varias acciones para continuar con el sistema de recomendaciones. Elija uno de los comandos para continuar con la accion deseada:")
    print('==================== 1 --> Recomendacion de cancion en base a los datos ingresados')
    print('==================== 2 --> Observar los datos ingresados')
    print('==================== 3 --> Ver generos de una cancion determinada')
    print('==================== 4 --> Salir')
    comandoIncorrecto = True
    while (comandoIncorrecto):
        comando = input("Comando: ")
        if (str(comando) == '1' or str(comando) == '2' or str(comando) == '3' or str(comando) == '4'):
            comandoIncorrecto = False
            if str(comando) == '1':
                recomendarCancion(elegidosConGeneros,nivelDeDificultad)
            elif str(comando) == '2':
                observarDatosIngresados(elegidosConGeneros,nivelDeDificultad)
            elif str(comando) == '3':
                verGenerosDeCancion()
            else:
                nosVimo = True
        else:
            print('Comando incorrecto!\n')
print('NOS VIMO!')