import re
import sys


# Este programa crea el vocabulario a partir del corpus que se le pase.
def createVocabulary():

    file = sys.argv[1]
    f = open(file, "r")
    vocabulary = set()

    for line in f:
        # Si la línea no está vacía.
        if line.strip():

            # Buscamos por medio del uso de expresiones regulares todas aquellas
            # que sean de naturaleza alfanumérica y las añadimos al vocabulario.
            if(len(re.findall("\w+", line)) > 0):
                coincidences = re.findall("\w+", line)
                for i in range(len(coincidences)):
                    coincidences[i] = re.sub(r'\s','',coincidences[i])
                vocabulary.update(coincidences)

            # Buscamos por medio del uso de expresiones regulares todas aquellas
            # que sean de naturaleza no alfanumérica y las añadimos al vocabulario.
            if(len(re.findall("\W+", line)) > 0):
                coincidences = re.findall("\W+", line)
                for i in range(len(coincidences)):
                    coincidences[i] = re.sub(r'\s','',coincidences[i])
                vocabulary.update(coincidences)
    f.close()

    # Escribimos en un fichero que hemos llamado vocabulario.txt todas las
    # coincidencias que hemos obtenido previamente.
    fich_vocabulario = open("vocabulario.txt", "w+")
    fich_vocabulario.write("Numero de palabras: " + str(len(vocabulary)) + "\n")
    vocabulary = sorted(vocabulary)
    for word in vocabulary:
        fich_vocabulario.write("Palabra: " + word + "\n")

    fich_vocabulario.close()

createVocabulary()
