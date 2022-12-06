import csv
import numpy as np
import pandas as pd

TRACKS_FILEPATH = 'Datasets/tracks_features.csv'
INDEX_ID_CANCIONES = 0
INDEX_NOMBRE_CANCIONES = 1
INDEX_NOMBRE_ARTISTAS = 4

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
                return ([], [], True)
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
                    print(count)
                    elegidos.append(current[count])
                    current.pop(count)
                    return (current, elegidos, False)
                else:
                    print('El Id elegido no esta presente entre los mostrados.\n')
    


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
    print(print('PARCIAL: ' + str(elegidos)))
print('FINAL: ' + str(elegidos))
