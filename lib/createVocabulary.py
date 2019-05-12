import re
import sys
import tweetProcessing


# Este programa crea el vocabulario a partir del corpus que se le pase.
def createVocabulary():

    file = "../" + sys.argv[1]
    f = open(file, "r")
    vocabulary = set()

    for line in f:
        # Si la línea no está vacía.
        if line.strip():
            line = tweetProcessing.processTweet(line)
            vocabulary.update(line)

    f.close()

    # Escribimos en un fichero que hemos llamado vocabulario.txt todas las
    # coincidencias que hemos obtenido previamente.
    fich_vocabulario = open("../vocabulario.txt", "w+")
    fich_vocabulario.write("Numero de palabras: " + str(len(vocabulary)) + "\n")
    vocabulary = sorted(vocabulary)

    if "" in vocabulary:
        vocabulary.remove("") #Eliminamos la cadena vacía.

    for word in vocabulary:
        fich_vocabulario.write("Palabra: " + word + "\n")

    fich_vocabulario.close()

createVocabulary()
