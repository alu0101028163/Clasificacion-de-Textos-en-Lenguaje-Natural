import sys


def compareSuccess():

    corpus_obj_file = "../" + sys.argv[1]
    corpus_clas_file = "../" + sys.argv[2]

    corpus_obj = open(corpus_obj_file,"r")
    corpus_clas = open(corpus_clas_file, "r")


    obj = []
    clas = []

    for line in corpus_obj:
        line = line.strip()
        word = line.split()
        obj += word

    for line in corpus_clas:
        line = line.strip()
        word = line.split()
        clas += word

    assert(len(obj) == len(clas))

    success = 0
    failure = 0

    for i in range(len(obj)):
        if(clas[i] == obj[i]):
            success += 1
        else:
             failure += 1

    print("PRECISSION IS EQUAL TO : " + str(((success) / (success + failure )) * 100 ) + " %")


    corpus_obj.close()
    corpus_clas.close()

compareSuccess()
