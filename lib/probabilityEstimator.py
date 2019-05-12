import math
import sys


def getCorpusDocuments(corpus_file_name):

    corpusDocuments = 0
    corpus = open(corpus_file_name, "r")

    for tweet in corpus:
        corpusDocuments += 1

    corpus.close()

    return corpusDocuments

def getCorpusWords(corpus_file_name):
    corpusWords = 0
    corpus = open(corpus_file_name, "r")

    for tweet in corpus:
        words = tweet.split()
        for word in words:
            corpusWords += 1

    corpus.close()

    return corpusWords

def probabilityEstimator():
        vocabulary_ =  "../" + sys.argv[1];
        vocabulary = open(vocabulary_, "r")
        corpus_ = "../" + sys.argv[2];
        # corpus = open(corpus_, "r")
        training_file_ = "../" + sys.argv[3];
        training_file = open(training_file_, "w+")

        vocabulary_size = vocabulary.readline()
        vocabulary_size = vocabulary_size.replace("Numero de palabras: ",'')

        # print(getCorpusDocuments(corpus_))
        # print(getCorpusWords(corpus_))

        corpus = open(corpus_, "r")

        training_file.write("Numero de documentos del corpus: " + str(getCorpusDocuments(corpus_)) + "\n")
        training_file.write("Numero de palabras del corpus: " + str(getCorpusWords(corpus_)) + "\n")

        for word in vocabulary:

            word = word.replace("Palabra: ", '')
            word = word.strip()
            word_frequency = 0

            corpus = open(corpus_, "r")
            corpus_size = 0

            for tweet in corpus:
                tweet = tweet.split()
                for w in tweet:
                    if(w == word):
                        word_frequency += 1
                    corpus_size += 1

            # print("CORPUS SIZE: " + str(corpus_size))
            # print("VOCABULARY SIZE: " + str(vocabulary_size))
            # print("DIVISION == " + word + " " + str(word_frequency + 1) +  "/" + str(int(corpus_size) + int(vocabulary_size) + 1))
            prob_logarithm = math.log((word_frequency + 1) / ((int(corpus_size) + int(vocabulary_size) + 1)))
            word_data = "Palabra: " + word.strip().ljust(10) + " Frec: " + str(word_frequency).ljust(5) + " LogProb: " + str(prob_logarithm) + "\n"
            training_file.write(word_data)

        vocabulary.close()
        corpus.close()
        training_file.close()

probabilityEstimator()
