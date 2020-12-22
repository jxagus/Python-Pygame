# FUNCION ELEJIDA FINALMENTE PARA FILTRAR VOCALES CON TILDES, LETRAS Ñ Y DIERESIS, ADEMAS DE TAMAÑO DE RENGLON (DESARROLLADA POR NOPSOTROS)
def filtrarTildesYtamaño(letra, archivo):
    ancho=48
    letra=[]
    for linea in archivo:
        linea=unicodedata.normalize("NFKD", linea).encode("ascii","ignore").decode("ascii")
        long=len(linea)
        if long<ancho:
            letra.append(linea)
    return letra

# FUNCION QUE TOMAMOS COMO SECUNDARIA IMPORTADA DE INTERNET PARA FILTAR UNICAMENTE CARACTERES (NO UTILIZADA)
def Tildes_y_OtrasLetras(s):
    reemplazo = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
        ("ü", "u"),
    )
    for a, b in reemplazo:
        tildes = tildes.replace(a, b).replace(a.upper(), b.upper())
    return s

# FUNCION UTILIZADA PARA SELECCIONAR RENGLONES MEDIANTE UN ACUMULADOR Y CONTADOR DE PALABRAS (DESARROLLADA POR NOSOTROS, NO UTILIZADA)
def cantPalabras(letra): #primera opcion
    acum=""
    cont=0
    for linea in letra:
        for palabra in linea:
            if palabra<10:
                acum=acum+palabra
                cont=cont+1
                letra.append(acum)
    return acum

# FUNCION UTILIZADA PARA SELECCIONAR RENGLONES MEDIANTE UN ACUMULADOR Y CONTADOR DE LETRAS (DESARROLLADA POR NOSOTROS, NO UTILIZADA)
def cantLetras(letra): #segunda opcion
    acum=""
    cont=0
    for palabra in letra:
        for letra in palabra:
            if cont<40:
                acum=acum+letra
                cont=cont+1
                letra.append(acum)


    return acum

# FUNCION UTILIZADA PARA DISCRIMINAR EL PRIMER RENGLON DE CADA CANCION Y ACUMULARLO EN LA LISTA artistaYcancion (DESARROLLADA POR NOSOTROS, NO UTILIZADA)
def primeraLinea(letra,artistaYcancion):
    artistaYcancion=[]
    for linea in range (len(letra)):
        if linea==0:
            artistaYcancion.append(letra[linea])
        return artistaYcancion[0]

# FUNCION IMPORTADA DE INTERNET Y DESARROLLADA POR NOSOTROS PARA AGREGAR SONIDOS Y MUSICA DE FONDO
def sonido(correctas):
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

