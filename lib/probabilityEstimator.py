import math
import re
import sys
import tweetProcessing


def create_dict(vocabulary_):

    vocabulary = open(vocabulary_, "r")
    vocabulary.readline() #Nº documentos del corpus

    dict = {}
    for tweet in vocabulary:
        word_regex = re.compile("Palabra:\s[+-]?(.+?)\s")
        word = word_regex.search(tweet)

        if(word):
              dict[word.group(1)] = 0

    vocabulary.close()

    return dict

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
        training_file_ = "../" + sys.argv[3];
        training_file = open(training_file_, "w+")

        vocabulary_size = vocabulary.readline()
        vocabulary_size = vocabulary_size.replace("Numero de palabras: ",'')
        vocabulary.close()


        vocabulary = create_dict(vocabulary_)

        corpus = open(corpus_, "r")

        training_file.write("Numero de documentos del corpus: " + str(getCorpusDocuments(corpus_)) + "\n")
        training_file.write("Numero de palabras del corpus: " + str(getCorpusWords(corpus_)) + "\n")

        corpus_size = 0
        for tweet in corpus:
            tweet = tweetProcessing.processTweet(tweet)
            for w in tweet:
                if w in vocabulary:
                    vocabulary[w] += 1
                corpus_size += 1

        for word in vocabulary:
            # print(str(vocabulary[word] + 1) +  " / " + str(corpus_size) + " + " + str(int(vocabulary_size)) + " + " + "1")
            prob_logarithm = math.log((vocabulary[word] + 1) / ((int(corpus_size) + int(vocabulary_size) + 1)))
            word_data = "Palabra: " + word.strip().ljust(10) + " Frec: " + str(vocabulary[word]).ljust(5) + " LogProb: " + str(prob_logarithm) + "\n"
            training_file.write(word_data)


        corpus.close()
        training_file.close()

probabilityEstimator()
