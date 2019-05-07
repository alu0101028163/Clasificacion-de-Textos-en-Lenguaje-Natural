import sys              # Command line arguments
import re               # Regular expressions
import numpy as np      # Arrays for high performance operations



# Esta función se encarga de tomar los tweets de entrada y clasificarlos en tres corpus:
# el corpus no troll (corpusNT), el corpus troll (corpusT) y por último el corpus que engloba
# los corpus previos al que se la llamado "corpustodo".
#

def load():
    file = sys.argv[1];
    f = open(file, "r")
    corpusT = open("corpusT.txt","w+")
    corpusNT = open("corpusNT.txt","w+")
    corpusTODO = open("corpustodo.txt", "w+")

    corpusT_n_tokens = 0
    corpusNT_n_tokens = 0

    corpusT_arr = []
    corpusNT_arr = []
    corpusTODO_arr = []

    for line in f:

        # Si la línea no está vacía.
        if line.strip():

            line = re.sub(r'@\w+','',line)      # Se eliminan las menciones
            line = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',line) # Se eliminan las URLs
            line = re.sub(r'\"','',line)      # Se eliminan las comillas
            words = line.split(",")      # Se separan las etiquetas y el contenido del tweet

            # El strip es necesario porque estamos comparando troll\n con troll.
            # Por lo tanto hacemos un strip() que devuelve las cadenas sin esos
            # saltos de línea finales.
            if(words[1].strip() == "troll".strip()):
                for word in words[0]:
                    corpusT_n_tokens += 1
                corpusT_arr.append(words[0] + "\n")
            else:
                for word in words[0]:
                    corpusNT_n_tokens += 1
                corpusNT_arr.append(words[0] + "\n")


            corpusTODO_arr.append(words[0] + "\n")


    corpusT.write(str(corpusT_n_tokens) + "\n")
    for word in corpusT_arr:
         corpusT.write(word)

    corpusNT.write(str(corpusNT_n_tokens) + "\n")
    for word in corpusNT_arr:
         corpusNT.write(word)

    corpusTODO.write(str(corpusT_n_tokens + corpusNT_n_tokens) + "\n")
    for word in corpusTODO_arr:
        corpusTODO.write(word)


    f.close()
    corpusT.close()
    corpusNT.close()
    corpusTODO.close()


load()
