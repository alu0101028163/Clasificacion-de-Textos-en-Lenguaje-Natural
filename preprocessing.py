import sys              # Command line arguments
import re               # Regular expressions
import numpy as np      # Arrays for high performance operations


def load():
    file = sys.argv[1];
    f = open(file, "r")
    corpusT = open("corpusT.txt","w+")
    corpusNT = open("corpusNT.txt","w+")
    corpusTODO = open("corpustodo.txt", "w+")

    for line in f:

        # Si la línea no está vacía.
        if line.strip():

            line = re.sub(r'@\w+','',line)      # Se eliminan las menciones
            line = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',line) # Se eliminan las URLs
            words = line.split(",")      # Se separan las etiquetas y el contenido del tweet



            #TODO: ¿Qué hace el strip?
            ''' El strip es necesario porque estamos comparando
            troll\n con troll. Por lo tanto hacemos un strip() que devuelve'''
            if(words[1].strip() == "troll".strip()):
                corpusT.write(words[0] + "\n")
            else:
                corpusNT.write(words[0] + "\n")

            corpusTODO.write(words[0] + "\n")

    f.close()
    corpusT.close()
    corpusNT.close()
    corpusTODO.close()


load()
