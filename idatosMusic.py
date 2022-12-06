import csv
import numpy as np
import pandas as pd
from difflib import SequenceMatcher

GENRES_FILEPATH = 'Datasets/data_by_genres.csv'

# Define index column in genres csv file
# df = pd.read_csv(GENRES_FILEPATH)
# df['id']=df.index
# df.to_csv(GENRES_FILEPATH)

def obtenerIndicesPorValoresAsc(value, objeto):
    retPrimero = []
    retSegundo = []
    retTercero = []
    index = 0

    while (index < 2664):
        if (objeto[index][1] != value):
          break
        retPrimero.append(objeto[index][0])
        index += 1
    value = objeto[index][1]
    while (index < 2664):
        if (objeto[index][1] != value):
          break
        retSegundo.append(objeto[index][0])
        index += 1
    value = objeto[index][1]
    while (index < 2664):
        if (objeto[index][1] != value):
          break
        retTercero.append(objeto[index][0])
        index += 1
    return (retPrimero, retSegundo, retTercero)

def obtenerIndicesPorValoresDesc(value, objeto):
    retPrimero = []
    retSegundo = []
    retTercero = []
    index = 2663
    while (index >= 0):
        if (objeto[index][1] != value):
          break
        retPrimero.append(objeto[index][0])
        index -= 1
    value = objeto[index][1]
    while (index >= 0):
        if (objeto[index][1] != value):
          break
        retSegundo.append(objeto[index][0])
        index -= 1
    value = objeto[index][1]
    while (index >= 0):
        if (objeto[index][1] != value):
          break
        retTercero.append(objeto[index][0])
        index -= 1
    return (retPrimero, retSegundo, retTercero)

# Declaracion e inicializacion de los vectores de atributos
idWithGenreName = [ [ '' for y in range( 2 ) ] for x in range( 2664 ) ]
danceability = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
energy = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
key = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
loudness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
speechiness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
acoustucness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
instrumentalness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
liveness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
valence = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
tempo = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]

for i in range(0,2664):
    danceability[i][0] = float(i)
    energy[i][0] = float(i)
    key[i][0] = float(i)
    loudness[i][0] = float(i)
    speechiness[i][0] = float(i)
    acoustucness[i][0] = float(i)
    instrumentalness[i][0] = float(i)
    liveness[i][0] = float(i)
    valence[i][0] = float(i)
    tempo[i][0] = float(i)
    
    danceability[i][1] = float(0)
    energy[i][1] = float(0)
    key[i][1] = float(0)
    loudness[i][1] = float(0)
    speechiness[i][1] = float(0)
    acoustucness[i][1] = float(0)
    instrumentalness[i][1] = float(0)
    liveness[i][1] = float(0)
    valence[i][1] = float(0)
    tempo[i][1] = float(0)


with open('Datasets/data_by_genres.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0 and line_count <= 2664:
            danceability[line_count-1][1] = float(row[3])
            energy[line_count-1][1] = float(row[5])
            key[line_count-1][1] = float(row[13])
            loudness[line_count-1][1] = float(row[8])
            speechiness[line_count-1][1] = float(row[9])
            acoustucness[line_count-1][1] = float(row[2])
            instrumentalness[line_count-1][1] = float(row[6])
            liveness[line_count-1][1] = float(row[7])
            valence[line_count-1][1] = float(row[11])
            tempo[line_count-1][1] = float(row[10])

        line_count += 1
    print('Termino de procesar los parametros...')


# Ordenamiento
danceability = np.array(danceability)
energy = np.array(energy)
key = np.array(key)
loudness = np.array(loudness)
speechiness = np.array(speechiness)
acoustucness = np.array(acoustucness)
instrumentalness = np.array(instrumentalness)
liveness = np.array(danceability)
valence = np.array(valence)
tempo = np.array(tempo)

danceability = danceability[danceability[:,1].argsort()]
energy = energy[energy[:,1].argsort()]
key = key[key[:,1].argsort()]
loudness = loudness[loudness[:,1].argsort()]
speechiness = speechiness[speechiness[:,1].argsort()]
acoustucness = acoustucness[acoustucness[:,1].argsort()]
instrumentalness = instrumentalness[instrumentalness[:,1].argsort()]
liveness = liveness[liveness[:,1].argsort()]
valence = valence[valence[:,1].argsort()]
tempo = tempo[tempo[:,1].argsort()]


# Esta funcion retorna, dado un valor de un atributo especifico, el conjunto de indices de generos (referenciados en el vector idWithGenreName)
# que mas cerca estan de ese valor en orden. Es decir, en la primera ubicacion de la tripla, se encuentra el/los generos que tienen valor mas 
# cercano al valor pasado, en la segunda ubicacion de la tupla los siguientes generos mas cercanos, y en la tercera el conjunto de los terceros
# mas cercanos
def generosPorValor(value, atributo):
    if (float(value) <= atributo[0][1]):
        return obtenerIndicesPorValoresAsc(atributo[0][1],atributo)
    elif (float(value) >= atributo[2663][1]):
        return obtenerIndicesPorValoresDesc(atributo[2663][1],atributo)
    else:
        retPrimero = []
        retSegundo = []
        retTercero = []
        index = 1
        found = False
        while (index < 2664 and (not found)):
            if (atributo[index][1] <= value):
                index += 1
            else:
                found = True
        i = 1
        found = False
        if ((atributo[index][1] - value) > (value - atributo[index-1][1])): # El valor esta mas cerca del mas chico
            retPrimero.append(atributo[index-1][0])
            while(index - 1 - i >= 0 and (not found)):
                if (atributo[index-1-i][1] == atributo[index-1][1]):
                    retPrimero.append(atributo[index-1-i][0])
                    i += 1
                else:
                    found = True
            if (index-1-i >= 0):
                valorSegundoInf = atributo[index-1-i][1]
                found = False
                while(index - 1 - i >= 0 and (not found)):
                    if (atributo[index-1-i][1] == valorSegundoInf):
                        retSegundo.append(atributo[index-1-i][0])
                        i += 1
                    else:
                        found = True
                if(index-1-i >= 0):
                    valorTeceroInf = atributo[index-1-i][1]
                    found = False
                    while(index - 1 - i >= 0 and (not found)):
                        if (atributo[index-1-i][1] == valorTeceroInf):
                            retTercero.append(atributo[index-1-i][0])
                            i += 1
                        else:
                            found = True
            
            valorPrimeroSup = atributo[index][1]    # Va a ir en retSegundo con valorSegundoInf
            found = False
            i = 0
            while(index+i < 2664 and (not found)):
                if (atributo[index+i][1] == valorPrimeroSup):
                    retSegundo.append(atributo[index+i][0])
                    i += 1
                else:
                    found = True
            if (index+i < 2664):
                valorSegundoSup = atributo[index+i][1]  # Va a ir en retTercero con valorTerceroInf
                found = False
                while(index+i < 2664 and (not found)):
                    if (atributo[index+i][1] == valorSegundoSup):
                        retTercero.append(atributo[index+i][0])
                        i += 1
                    else:
                        found = True
        else: # El valor esta mas cerca del mas grande
            retPrimero.append(atributo[index][0])
            while(index + i < 2664 and (not found)):
                if (atributo[index+i][1] == atributo[index][1]):
                    retPrimero.append(atributo[index+i][0])
                    i += 1
                else:
                    found = True
            if (index+i < 2664):
                valorSegundoSup = atributo[index+i][1]
                found = False
                while(index+i < 2664 and (not found)):
                    if (atributo[index+i][1] == valorSegundoSup):
                        retSegundo.append(atributo[index+i][0])
                        i += 1
                    else:
                        found = True
                if (index+i < 2664):
                    valorTerceroSup = atributo[index+i][1]
                    found = False
                    while(index+i < 2664 and (not found)):
                        if (atributo[index+i][1] == valorTerceroSup):
                            retTercero.append(atributo[index+i][0])
                            i += 1
                        else:
                            found = True
            valorPrimeroInf = atributo[index-1][1]  # Va a ir en retSegundo con valorSegundoSup
            found = False
            i = 0
            while(index - 1 - i >= 0 and (not found)):
                if (atributo[index-1-i][1] == valorPrimeroInf):
                    retSegundo.append(atributo[index-1-i][0])
                    i += 1
                else:
                    found = True
            if(index-1-i >= 0):
                valorSegundoInf = atributo[index-1-i][1]  # Va a ir en retTercero con valorTerceroSup
                found = False
                while(index - 1 - i >= 0 and (not found)):
                    if (atributo[index-1-i][1] == valorSegundoInf):
                        retTercero.append(atributo[index-1-i][0])
                        i += 1
                    else:
                        found = True
        return (retPrimero, retSegundo, retTercero)

def generosPorAtributo (value, atributo):
    if (atributo == 'danceability'):
       return generosPorValor(value, danceability)
    elif (atributo == 'energy'):
        return generosPorValor(value, energy)
    elif (atributo == 'key'):
        return generosPorValor(value, key)
    elif (atributo == 'loudness'):
        return generosPorValor(value, loudness)
    elif (atributo == 'speechiness'):
        return generosPorValor(value, speechiness)
    elif (atributo == 'acoustucness'):
        return generosPorValor(value, acoustucness)
    elif (atributo == 'instrumentalness'):
        return generosPorValor(value, instrumentalness)
    elif (atributo == 'liveness'):
        return generosPorValor(value, liveness)
    elif (atributo == 'valence'):
        return generosPorValor(value, valence)
    elif (atributo == 'tempo'):
        return generosPorValor(value, tempo)



# PROXIMOS PASOS
#   1- HACER FUNCION TAL QUE, DADO UN CONJUNTO DE VALORES DE ATRIBUTOS, RETORNE LA INTERSECCION DE GENEROS QUE INTERESAN EN BASE A LA BUSQUEDA EN CADA UNO DE LOS ARRAYS DE ATRIBUTOS
#   2- OTRA POSIBLE FUNCIONALIDAD (VISTO LO QUE ESTOY HACIENDO) ES QUE EL USUARIO INGRESE UNA CANCION Y EL SISTEMA RETORNA LOS GENEROS QUE MAS SE APROXIMAN A LA MISMA