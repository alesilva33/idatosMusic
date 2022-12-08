import csv
import numpy as np
import pandas as pd
from manejoDeGeneros import obtenerGenerosDeCancion

# TRACKS_FILEPATH = 'Datasets/tracks_features.csv'
TRACKS_FILEPATH = 'Datasets/integratedData.csv'
INDEX_ID_CANCIONES = 0
INDEX_NOMBRE_CANCIONES = 1
INDEX_NOMBRE_ARTISTAS = 2
INDEX_ALBUM = 7
INDEX_DANCEABILITY = 8
INDEX_ACOUSTUCNESS = 11
INDEX_ENERGY = 9
INDEX_KEY = 10
INDEX_INSTRUMENTALNESS = 12
INDEX_VALENCE = 13
INDEX_TEMPO = 14
INDEX_DIFICULTAD = 3
INDEX_TONO = 4
INDEX_CAPO = 5
INDEX_TUNING = 6
INDEX_LYRICS = 17
INDEX_ANIO_CANCION = 16
INDEX_DURACION = 15

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
                aux.append(row[INDEX_DANCEABILITY])
                aux.append(row[INDEX_ACOUSTUCNESS])
                aux.append(row[INDEX_ENERGY])
                aux.append(row[INDEX_KEY])
                aux.append(row[INDEX_INSTRUMENTALNESS])
                aux.append(row[INDEX_VALENCE])
                aux.append(row[INDEX_TEMPO])
                ret.append(aux)
            if indexDesde + 4 == line_count:
                break
            line_count += 1
    return ret

def mensajeDeTituloDeCanciones():
    print(' - i {id} --> Comando para seleccionar una cancion. {id} es el identificador mostrado en las canciones expuestas.\n - r      --> Comando para desplegar 5 canciones mas.\n\n')
    print('========== CANCIONES ==========')
    print('---------- ID ---------- NOMBRE ---------- ARTISTAS ----------')

def mensajesBase(numero):
    txt = ''
    if (numero == 1):
       txt = ' Seleccione 1 cancion, '
    else:
        txt =  ' Seleccione ' + str(numero) + ' canciones, '
    print(txt + 'aca tenes 5 para elegir.\n\n')
    mensajeDeTituloDeCanciones()

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
        elem.append(obtenerGenerosDeCancion({'danceability': float(elem[3]), 'acoustucness': float(elem[4]), 'energy': float(elem[5]), 'key': float(elem[6]), 'instrumentalness': float(elem[7]), 'valence': float(elem[8]), 'tempo': float(elem[9])}))
        # elem.append(obtenerGenerosDeCancion({'danceability': 0.47, 'acoustucness': 0.0261, 'energy': 0.978, 'key': 7, 'instrumentalness': 1.09e-05, 'valence': 0.35600000000000004, 'tempo': 117.906}))
        ret.append(elem)
    return ret

def obtenerListaDeGenerosPrincipales(elegidosConGeneros):
    ret = []
    for elem in elegidosConGeneros:
        for gen in elem[10][0]:
            ret.append(gen)
    return ret

def presentarDatosDeCancionElegida(cancionElegida):
    if (cancionElegida == ''):
        print('\n---------- NO SE PUEDEN REALIZAR MAS RECOMENDACIONES. NO SE HAN ENCONTRADO CANCIONES CON EL MISMO NIVEL DE DIFICULTAD DEL INGRESADO POR EL USUARIO QUE COMPARTAN GENERO CON LA CANCIONES INGRESADAS POR EL MISMO ----------\n')
    else:
        print('\n---------- DATOS DE CANCION RECOMENDADA ----------\n')
        print(' ***** Nombre de la cancion: ' + str(cancionElegida[INDEX_NOMBRE_CANCIONES]))
        print(' ***** Album: ' + str(cancionElegida[INDEX_ALBUM]))
        print(' ***** Artista: ' + str(cancionElegida[INDEX_NOMBRE_ARTISTAS]))
        print(' ***** Año de la cancion: ' + str(cancionElegida[INDEX_ANIO_CANCION]))
        print(' ***** Duracion de la cancion (en segundos): ' + str(cancionElegida[INDEX_DURACION]))
        print(' ***** Dificultad de la cancion: ' + str(cancionElegida[INDEX_DIFICULTAD]))
        print(' ***** Tono de la cancion: ' + str(cancionElegida[INDEX_TONO]))
        print(' ***** Capo de la cancion: ' + str(cancionElegida[INDEX_CAPO]))
        print(' ***** Tunning de la cancion: ' + str(cancionElegida[INDEX_TUNING]))
        print(' ***** Letra de la cancion: ' + str(cancionElegida[INDEX_LYRICS]))
        print('\n\n')

def recomendarCancion(elegidosConGeneros, nivelDeDificultad, indexDesde):
    listaDeGenerosPrincipales = obtenerListaDeGenerosPrincipales(elegidosConGeneros)
    with open(TRACKS_FILEPATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        salir = False
        cancionElegida = ''
        for row in csv_reader:
            if line_count >= indexDesde:
                if (row[INDEX_DIFICULTAD] == nivelDeDificultad):
                    generos = obtenerGenerosDeCancion({'danceability': float(row[INDEX_DANCEABILITY]), 'acoustucness': float(row[INDEX_ACOUSTUCNESS]), 'energy': float(row[INDEX_ENERGY]), 'key': float(row[INDEX_KEY]), 'instrumentalness': float(row[INDEX_INSTRUMENTALNESS]), 'valence': float(row[INDEX_VALENCE]), 'tempo': float(row[INDEX_TEMPO])})
                    for gen in generos[0]:
                        if (listaDeGenerosPrincipales.count(gen) > 0):
                            cancionElegida = row
                            salir = True
                            break
            line_count += 1
            if salir:
                break
        presentarDatosDeCancionElegida(cancionElegida)
    return line_count

def stringDeGeneros(generos):
    stringGeneros = ''
    primero = True
    for gen in generos:
        if (primero):
            primero = False
            stringGeneros = str(gen)
        else:
            stringGeneros += ', ' + str(gen)
    if (primero):
        stringGeneros = 'NO TIENE'
    return stringGeneros

def observarDatosIngresados(elegidosConGeneros,nivelDeDificultad = ''):
    print('\n---------- NOMBRE ---------- ARTISTAS ---------- GENEROS ---------- GENEROS SIMILARES ---------- GENEROS MENOS SIMILARES\n')
    for elem in elegidosConGeneros:
        nombre = str(elem[1])
        artista = str(elem[2])
        generos = stringDeGeneros(elem[10][0])
        generosSimilares = stringDeGeneros(elem[10][1])
        generosMenosSimilares = stringDeGeneros(elem[10][2])
        print('---------- ' + nombre + ' ---------- ' + artista + ' ---------- ' + generos + ' ---------- ' + generosSimilares + ' ---------- ' + generosMenosSimilares)
    print('\n')
    if nivelDeDificultad != '':
        print(' ******** NIVEL DE DIFICULTAD: ' + nivelDeDificultad + '\n\n')
    else:
        print('\n')

def verGenerosDeCancion():
    elegidosConGeneros = eleccionDeCanciones(1)
    observarDatosIngresados(elegidosConGeneros)


def eleccionDeCanciones(numero):
    index = 1
    elegidos = []
    elementoElegido = False
    while (len(elegidos) < numero):
        mensajesBase(numero)
        if not elementoElegido:
            current = leerDelCsv(index)
            index += 5
            (current, elegidos, recargar) = manejoDeComandos(current, elegidos)
        else:
            (current, elegidos, recargar) = manejoDeComandos(current, elegidos)
        elementoElegido = not recargar
    return generosDeCancionesElegidas(elegidos)

# MAIN

print('==================== BIENVENIDO A IDatos Music ====================')
elegidosConGeneros = eleccionDeCanciones(5)

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
print('\nYa ha terminado el seteo inicial de datos!\n\n')

nosVimo = False
lineaDesdeDondeObtenerRecomendacion = 1
while(not nosVimo):
    print("A continuacion cuenta con varias acciones para continuar con el sistema de recomendaciones. Elija uno de los comandos para continuar con la accion deseada:")
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
                lineaDesdeDondeObtenerRecomendacion = recomendarCancion(elegidosConGeneros,nivelDeDificultad, lineaDesdeDondeObtenerRecomendacion)
            elif str(comando) == '2':
                observarDatosIngresados(elegidosConGeneros,nivelDeDificultad)
            elif str(comando) == '3':
                verGenerosDeCancion()
            else:
                nosVimo = True
        else:
            print('Comando incorrecto!\n')
print('\n\nNOS VIMO!')