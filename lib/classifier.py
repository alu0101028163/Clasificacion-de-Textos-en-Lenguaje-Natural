import sys
import re

def create_dict(learning_file):
    dict = {}
    for tweet in learning_file:
        word_regex = re.compile("Palabra:\s[+-]?(.+?)\s")
        prob_regex = re.compile("LogProb:\s[+-]?((\d+).?(\d+))")
        word = word_regex.search(tweet)
        prob = prob_regex.search(tweet)

        if(word):
          if(prob):
              dict[word.group(1)] = float(prob.group(1))


    return dict


def classifier():

    corpus_ = "../" + sys.argv[1];
    corpus = open(corpus_, "r")
    learning_file1_ = "../" + sys.argv[2];
    learning_file1 = open(learning_file1_, "r")
    learning_file2_ = "../" + sys.argv[3];
    learning_file2 = open(learning_file2_, "r")

    learning_set1 = create_dict(learning_file1)
    learning_set2 = create_dict(learning_file2)

    for tweet in corpus:
        tweet = re.sub(r'@\w+','',tweet)      # Se eliminan las menciones
        tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',tweet) # Se eliminan las URLs
        tweet = re.sub(r'\"','',tweet)      # Se eliminan las comillas
        words = tweet.split()
        probability = 0
        for word in words:
            if word in learning_set1:
                probability = learning_set1[word]
            else:
                print("Missing: " + word)


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
