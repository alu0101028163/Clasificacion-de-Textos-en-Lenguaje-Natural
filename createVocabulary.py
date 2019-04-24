import re
import sys



def createVocabulary():

    file = sys.argv[1]
    f = open(file, "r")
    vocabulary = set()

    for line in f:
        # Si la línea no está vacía.
        if line.strip():
            # print(line)
            if(len(re.findall("\w+", line)) > 0):
                coincidences = re.findall("\w+", line)
                for i in range(len(coincidences)):
                    coincidences[i] = re.sub(r'\s','',coincidences[i])
                vocabulary.update(coincidences)

            if(len(re.findall("\W+", line)) > 0):
                coincidences = re.findall("\W+", line)
                for i in range(len(coincidences)):
                    coincidences[i] = re.sub(r'\s','',coincidences[i])
                vocabulary.update(coincidences)
    f.close()

    fich_vocabulario = open("vocabulario.txt", "w+")
    fich_vocabulario.write(str(len(vocabulary)))
    for word in vocabulary:
        fich_vocabulario.write(word + "\n")

    fich_vocabulario.close()

createVocabulary()
