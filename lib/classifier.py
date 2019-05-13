import sys
import re
import math
import tweetProcessing

def create_dict(learning_file_):

    learning_file = open(learning_file_, "r")
    learning_file.readline() #Nº documentos del corpus
    learning_file.readline() #Nº de palabras del corpus

    dict = {}
    for tweet in learning_file:
        word_regex = re.compile("Palabra:[+-]?(.+?)\s")
        prob_regex = re.compile("LogProb:([+-]?(\d+).?(\d+))")
        word = word_regex.search(tweet)
        prob = prob_regex.search(tweet)

        if(word):
          if(prob):
              dict[word.group(1)] = float(prob.group(1))

    learning_file.close()

    return dict


def get_sizes(learning_file_):

    learning_file = open(learning_file_, "r")

    corpus_documents = learning_file.readline() #Nº documentos del corpus
    corpus_documents = corpus_documents.strip()

    corpus_words = learning_file.readline()
    corpus_words = corpus_words.strip()

    corpus_documents = corpus_documents.replace("Numero de documentos del corpus:", '')
    corpus_words = corpus_words.replace("Numero de palabras del corpus:", '')

    learning_file.close()

    return float(corpus_documents), float(corpus_words)
    # return float(corpus_documents),float(corpus_words)



def classifier():

    corpus_ = "../" + sys.argv[1];
    corpus = open(corpus_, "r")

    # learning_file1_ = "../" + sys.argv[2];
    # learning_file2_ = "../" + sys.argv[3];

    learning_file1_ = "../aprendizajeT.txt";
    learning_file2_ = "../aprendizajenT.txt";

    classification_file = "../" + sys.argv[2];
    classification = open(classification_file,'w+')

    learning_set1 = create_dict(learning_file1_)
    learning_set2 = create_dict(learning_file2_)

    set1_corpus_documents, set1_corpus_words = get_sizes(learning_file1_)
    set2_corpus_documents, set2_corpus_words = get_sizes(learning_file2_)

    learning_file1 = open(learning_file1_, "r")
    learning_file2 = open(learning_file2_, "r")

    set1_counter = 0
    set2_counter = 0

    corpus_documents = 0

    for tweet in corpus:
        corpus_documents += 1

    corpus = open(corpus_, "r")

    for tweet in corpus:

        words = tweetProcessing.processTweet(tweet)

        probability_set1 = 1
        for word in words:
            if word in learning_set1:
                probability_set1 += learning_set1[word]
            else:
                probability_set1 += learning_set1['UNK']

        probability_set1 += math.log( set1_corpus_documents / (set1_corpus_documents + set2_corpus_documents) )

        probability_set2 = 1
        for word in words:
            if word in learning_set2:
                probability_set2 += learning_set2[word]
            else:
                probability_set2 += learning_set2['UNK']

        probability_set2 += math.log( set2_corpus_documents / (set1_corpus_documents + set2_corpus_documents) )


        if(probability_set1 > probability_set2):
            set1_counter += 1
            classification.write("T\n")
        else:
            set2_counter += 1
            classification.write("nT\n")

    print("Troll : " + str(set1_counter) + " No Troll: " + str(set2_counter))


    corpus.close()
    learning_file1.close()
    learning_file2.close()
    classification.close()

classifier()
