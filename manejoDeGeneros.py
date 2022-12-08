import csv
import numpy as np
import pandas as pd

GENRES_FILEPATH = 'Datasets/data_by_genres.csv'

# # Define index column in genres csv file
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
acoustucness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
instrumentalness = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
valence = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]
tempo = [ [ 0.0 for y in range( 2 ) ] for x in range( 2664 ) ]

for i in range(0,2664):
    idWithGenreName[i][0] = str(float(i))
    danceability[i][0] = float(i)
    energy[i][0] = float(i)
    key[i][0] = float(i)
    acoustucness[i][0] = float(i)
    instrumentalness[i][0] = float(i)
    valence[i][0] = float(i)
    tempo[i][0] = float(i)
    
    danceability[i][1] = float(0)
    energy[i][1] = float(0)
    key[i][1] = float(0)
    acoustucness[i][1] = float(0)
    instrumentalness[i][1] = float(0)
    valence[i][1] = float(0)
    tempo[i][1] = float(0)


with open('Datasets/data_by_genres.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0 and line_count <= 2664:
            idWithGenreName[line_count-1][1] = str(row[1])
            danceability[line_count-1][1] = float(row[3])
            energy[line_count-1][1] = float(row[5])
            key[line_count-1][1] = float(row[13])
            acoustucness[line_count-1][1] = float(row[2])
            instrumentalness[line_count-1][1] = float(row[6])
            valence[line_count-1][1] = float(row[11])
            tempo[line_count-1][1] = float(row[10])

        line_count += 1


# Ordenamiento
danceability = np.array(danceability)
energy = np.array(energy)
key = np.array(key)
acoustucness = np.array(acoustucness)
instrumentalness = np.array(instrumentalness)
valence = np.array(valence)
tempo = np.array(tempo)

danceability = danceability[danceability[:,1].argsort()]
energy = energy[energy[:,1].argsort()]
key = key[key[:,1].argsort()]
acoustucness = acoustucness[acoustucness[:,1].argsort()]
instrumentalness = instrumentalness[instrumentalness[:,1].argsort()]
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
    elif (atributo == 'acoustucness'):
        return generosPorValor(value, acoustucness)
    elif (atributo == 'instrumentalness'):
        return generosPorValor(value, instrumentalness)
    elif (atributo == 'valence'):
        return generosPorValor(value, valence)
    elif (atributo == 'tempo'):
        return generosPorValor(value, tempo)

# Funcion que recibe un conjunto de atributos como objeto (ej: {'danceability': 0.906, 'acoustucness': 0.036}) y retorna una tripleta de arrays, donde el primer array de la tripleta 
# muestra los identificadores de los  generos que mas coinciden con los atributos recibidos; en el segundo array de la tripleta los siguientes que mas coinciden; 
# y en el tercer array los ultimos.
# Regla general para obtener los elementos de la tripleta:
#   * Primer array de la tripleta:
#       - Valor del primer nivel de un atributo coincide con al menos un valor del primer de otro/s atributo/s
#       - Valor del primer nivel de un atributo coincide con al menos dos del segundo nivel de otros atributos
#       - Valor del primer nivel de un atributo coincide con uno del segundo nivel y al menos 2 del tercer nivel
#   * Segundo array de la tripleta:
#       - Valor del primer nivel de un atributo coincide con uno del segundo nivel y uno del tercer nivel
#       - Valor del segundo nivel de un atributo coincide con al menos un valor del segundo nivel de otro/s atributo/s
#       - Valor del segundo nivel de un atributo coincide con al menos 2 valores del tercer nivel de otros atributos
#   * Tercer array de la tripleta  
#       - Valor del segundo nivel de un atributo coincide con un valor del tercer nivel de otro atributo
#       - Dos o mas valores del tercer nivel de atributos coinciden en ese mismo nivel
# En caso que el primer array de la tripleta quede vacio, si el segundo array de la tripleta no esta vacio, entonces este pasa a ser el primero, y el tercero pasar a ser el segundo (en 
# caso que no sea vacio tampoco). El mismo desplazamiento sucede si el segundo es vacio y el tercero no es vacio.
# Lo ideal es que esta funcion reciba todos los atributos (la idea seria que capaz se obtengan los atributos de una cancion especifica)
def interseccionDeVariosAtributos(atributos):
    aux = []
    if (atributos.get('danceability') != None): 
        aux.append(generosPorAtributo(atributos.get('danceability'),'danceability'))
    if (atributos.get('energy') != None):
        aux.append(generosPorAtributo(atributos.get('energy'),'energy'))
    if (atributos.get('key') != None): 
        aux.append(generosPorAtributo(atributos.get('key'),'key'))
    if (atributos.get('acoustucness') != None): 
        aux.append(generosPorAtributo(atributos.get('acoustucness'),'acoustucness'))
    if (atributos.get('instrumentalness') != None): 
        aux.append(generosPorAtributo(atributos.get('instrumentalness'),'instrumentalness'))
    if (atributos.get('valence') != None): 
        aux.append(generosPorAtributo(atributos.get('valence'),'valence'))
    if (atributos.get('tempo') != None): 
        aux.append(generosPorAtributo(atributos.get('tempo'),'tempo'))
    ret = []
    ret.append(getGenerosPrimeroNivelDeCoincidencia(aux))
    ret.append(getGenerosSegundoNivelDeCoincidencia(aux))
    ret.append(getGenerosTercerNivelDeCoincidencia(aux))
    # Desplazamiento en caso de que un nivel superior este vacio
    if (len(ret[0]) == 0):
        if (len(ret[1]) > 0):
            ret[0] = ret[1]
            if (len(ret[2]) > 0):
                ret[1] = ret[2]
                ret[2] = []
            else:
                ret[1] = []
        elif (len(ret[2]) > 0):
            ret[0] = ret[2]
            ret[2] = []
    elif (len(ret[1]) == 0 and len(ret[2]) > 0):
        ret[1] = ret[2]
        ret[2] = []
    return ret
    
def getGenerosPrimeroNivelDeCoincidencia(generos):
    ret = []
    (primerNivel, segundoNivel, tercerNivel) = agruparPorNivel(generos)
    for elem in primerNivel:
        if (ret.count(elem) == 0 and (primerNivel.count(elem) > 1 or segundoNivel.count(elem) > 1 or (segundoNivel.count(elem) == 1 and tercerNivel.count(elem) > 1))):
            ret.append(elem)
    return ret

def getGenerosSegundoNivelDeCoincidencia(generos):
    ret = []
    (primerNivel, segundoNivel, tercerNivel) = agruparPorNivel(generos)
    for elem in segundoNivel:
        if (ret.count(elem) == 0 and ((primerNivel.count(elem) == 1 and tercerNivel.count(elem) == 1) or segundoNivel.count(elem) > 1 or tercerNivel.count(elem) > 1)):
            ret.append(elem)
    return ret

def getGenerosTercerNivelDeCoincidencia(generos):
    ret = []
    (primerNivel, segundoNivel, tercerNivel) = agruparPorNivel(generos)
    for elem in tercerNivel:
        if (ret.count(elem) == 0 and (segundoNivel.count(elem) == 1 or tercerNivel.count(elem) > 1)):
            ret.append(elem)
    return ret

def agruparPorNivel(generos):
    primerNivel = []
    segundoNivel = []
    tercerNivel = []
    for gen in generos:
        for elem in gen[0]:
            primerNivel.append(elem)
        for elem in gen[1]:
            segundoNivel.append(elem)
        for elem in gen[2]:
            tercerNivel.append(elem)
    return (primerNivel, segundoNivel, tercerNivel)

# ESTE ES EL METODO QUE DEBE SER LLAMADO PARA OBTENER EL/LOS GENEROS DE LAS CANCIONES
def obtenerGenerosDeCancion(atributos):
    indicesDeGeneros = interseccionDeVariosAtributos(atributos)
    ret = []
    for gen in indicesDeGeneros:
        aux = []
        for elem in gen:
            aux.append(idWithGenreName[int(elem)][1])
        ret.append(aux)
    return ret