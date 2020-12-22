from configuracion import *
import random
import math
import unicodedata
import pygame



def lectura(archivo, letra, artistaYcancion): #se queda solo con los oraciones de cierta longitud y filtra tildes por ej
    #artistaYcancion toman primer linea de archivo.
    #letra toma la letra a partir de la 2da linea-
    cont = 0
    print(archivo)
    for linea in archivo: #Recorre cada línea de archivo
        linea=unicodedata.normalize("NFKD", linea).encode("ascii","ignore").decode("ascii") #filtro tildes, ñ y dieresis
        linea=linea.rstrip("\n") #Elimina los saltos de línea
        if(cont==0):
            for elem in linea.split(";"): #recorre los elementos de la línea con índice cero
                artistaYcancion.append(elem) #se cargan los elementos en la lista artistaYcancion
        else:
            if len(linea) * TAMANNO_LETRA < ANCHO: #solo pasan las líneas que entran en el ancho de la pantalla
                letra.append(linea) #cargo las lineas en la lista letra
        cont = cont + 1
    #print("respuesta", artistaYcancion)
    return(artistaYcancion,letra)


def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
        al_azar=random.randrange(0,len(letra)-1) #Elije un número entre 0 y la longitud de la línea-1 para que no me tome la última línea, ya que debo mostrar 2 líenas en pantalla
        siguiente=al_azar+1 #guardo el índice de la línea siguiente
        lista=[] #En lista guarda las 2 líneas que se muestran en pantalla
        lista.append(letra[al_azar])
        lista.append(letra[siguiente])
        return lista


def puntos(n): #devuelve el puntaje, segun seguidilla
    if n>0:
        return (2**n)
    else:
        return -2


def esCorrecta(palabraUsuario,artistaYcancion, correctas): #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    for i in range (len(artistaYcancion)): #Recorre la lista artistaYcancion
        if palabraUsuario==artistaYcancion[i]: #compara lo que ingresa el usuario con los elementos de artistaYcancion
            return puntos(1) #si palabraUsuario es igual a algún elemento de la lista, suma puntos
    return puntos(0) #por este lado resta puntos si el usuario ingresa algo incorrecto



def sonido(correctas): #esta función reproduce el sonido dependiendo de la cantidad de aciertos
    if correctas==1:
        pygame.init()
        sound=pygame.mixer.Sound("correctas1.mp3")
        return sound.play()
    if correctas>1:
        pygame.init()
        sound=pygame.mixer.Sound("seguidilla.mp3")
        return sound.play()
    if correctas==0:
        pygame.init()
        sound=pygame.mixer.Sound("correctas0.mp3")
        return sound.play()


