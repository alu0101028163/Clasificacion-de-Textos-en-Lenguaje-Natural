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
        word_regex = re.compile("Palabra:\s[+-]?(.+?)\s")
        prob_regex = re.compile("LogProb:\s([+-]?(\d+).?(\d+))")
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

    corpus_documents = corpus_documents.replace("Numero de documentos del corpus: ", '')
    corpus_words = corpus_words.replace("Numero de palabras del corpus: ", '')

    learning_file.close()

    return float(corpus_documents), float(corpus_words)
    # return float(corpus_documents),float(corpus_words)



def classifier():

    corpus_ = "../" + sys.argv[1];
    corpus = open(corpus_, "r")

    learning_file1_ = "../" + sys.argv[2];
    learning_file2_ = "../" + sys.argv[3];

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

    # for key in learning_set2:
    #     print(key + " " + str(learning_set2[key]))
    #
    # print(" ")
    # for key in learning_set1:
    #     print(key + " " + str(learning_set1[key]))
    #

    for tweet in corpus:

        print(" ")
        print(tweet)
        words = tweetProcessing.processTweet(tweet)

        probability_set1 = 1
        for word in words:
            if word in learning_set1:
                probability_set1 += learning_set1[word]
                print(probability_set1)
            else:
                print("MISSIN WORD: " + word)

        probability_set1 += math.log( set1_corpus_documents / (set1_corpus_documents + set2_corpus_documents) )
        print(probability_set1)

        print("--------------------------------")
        probability_set2 = 1
        for word in words:
            if word in learning_set2:
                probability_set2 += learning_set2[word]
                print(probability_set2)
            else:
                print("MISSIN WORD: " + word)

        probability_set2 += math.log( set2_corpus_documents / (set1_corpus_documents + set2_corpus_documents) )
        print(probability_set2)

        if(probability_set1 > probability_set2):
            set1_counter += 1
        else:
            set2_counter += 1

    print("SET1: " + str(set1_counter) + " SET2: " + str(set2_counter))
    # print(str(math.log(set2_corpus_documents / (set1_corpus_documents + set2_corpus_documents))))

    # for tweet in corpus:
    #
    #     #P(Troll|"thanks  the nerd in me is overjoyed") = P("thanks  the nerd in me is overjoyed"|Troll) x P(Troll) /
    #                                                      #P("thanks the nerd in me is overjoyed")
    #     #P(NTroll|"thanks  the nerd in me is overjoyed") = P("thanks  the nerd in me is overjoyed"|NTroll) x P(NTroll) /
    #                                                      #P("thanks the nerd in me is overjoyed")
    #
    #     #P("thanks  the nerd in me is overjoyed"|Troll)
    #     #=P("thanks"|troll) x P("the"|troll) x P("nerd"|troll) x P("in"|troll) ...
    #     #=log(P("thanks"|troll)) x log(P("the"|troll)) x log(P("nerd"|troll)) x log(P("in"|troll)) ...
    #
    #     for word in tweet:


    corpus.close()
    learning_file1.close()
    learning_file2.close()

classifier()
