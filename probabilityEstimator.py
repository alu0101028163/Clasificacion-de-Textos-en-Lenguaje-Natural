import math
import sys


def probabilityEstimator():
        vocabulary_ = sys.argv[1];
        vocabulary = open(vocabulary_, "r")
        corpus_ = sys.argv[2];
        corpus = open(corpus_, "r")
        training_file_ = sys.argv[3];
        training_file = open(training_file_, "w+")

        vocabulary_size = vocabulary.readline()
        vocabulary_size = vocabulary_size.replace("Numero de palabras: ",'')
        corpus_size = corpus.readline()

        #TODO: No entiendo bien qué hay que poner en esta cabecera.
        training_file.write("Numero de documentos del corpus: " + str(len(sys.argv) - 1) + "\n")
        training_file.write("Numero de palabras del corpus: " + str(corpus_size))

        for word in vocabulary:

            word = word.replace("Palabra: ", '')
            word_frequency = 0

            corpus = open(corpus_, "r")
            for tweet in corpus:
                if word in tweet:
                    word_frequency += 1

            prob_logarithm = math.log((word_frequency + 1) / (int(corpus_size) + int(vocabulary_size) + 1))
            word_data = "Palabra: " + word.strip().ljust(10) + " Frec: " + str(word_frequency).ljust(5) + " LogProb: " + str(prob_logarithm) + "\n"
            # word_data = word.strip() + str(word_frequency) + str(prob_logarithm) + "\n"
            training_file.write(word_data)

        vocabulary.close()
        corpus.close()
        training_file.close()

probabilityEstimator()
