import re


def processTweet(tweet):

    tweet = re.sub(r'@\w+','',tweet)      # Se eliminan las menciones
    tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',tweet) # Se eliminan las URLs
    tweet = re.sub(r'\"','',tweet)      # Se eliminan las comillas
    words = tweet.split()

    tweet_arr = []

    # Buscamos por medio del uso de expresiones regulares todas aquellas
    # palabras con apóstrofes
    if(len(re.findall("[a-zA-Z]+'[a-zA-Z]+", tweet)) > 0):
        coincidences = re.findall("[a-zA-Z]+'[a-zA-Z]+", tweet)
        for i in range(len(coincidences)):
            coincidences[i] = re.sub(r'\s','',coincidences[i])
        tweet_arr += coincidences
        tweet = re.sub(r'[a-zA-Z]+\'[a-zA-Z]+','',tweet)

    # Buscamos por medio del uso de expresiones regulares todas aquellas
    # cadenas unicamente compuestas por letras.
    if(len(re.findall("[a-zA-Z]+", tweet)) > 0):
        coincidences = re.findall("[a-zA-Z]+", tweet)
        for i in range(len(coincidences)):
            coincidences[i] = re.sub(r'\s','',coincidences[i])
        tweet_arr += coincidences
        tweet = re.sub(r'[a-zA-Z]+','',tweet)

    # Buscamos por medio del uso de expresiones regulares todas aquellas
    # cadenas que cacen con emoticonos.
    if(len(re.findall("(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", tweet)) > 0):
        coincidences = re.findall("(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", tweet)
        for i in range(len(coincidences)):
            coincidences[i] = re.sub(r'\s','',coincidences[i])
        tweet_arr += coincidences
        tweet = re.sub(r'(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)','',tweet)

    return tweet_arr

tweet_arr = processTweet("\"damn work fire wall. can't go to myspace. :(\"")
for word in tweet_arr:
    print(word)
