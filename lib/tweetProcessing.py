import re

def processTweet(tweet):

    tweet = re.sub(r'@\w+','',tweet)      # Se eliminan las menciones
    # tweet = re.sub(r'#\w+','',tweet)      # Se eliminan los hashtag.
    tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',tweet) # Se eliminan las URLs
    tweet = re.sub(r'\"','',tweet)       # Se eliminan las comillas
    words = tweet.split(",")            # Se separan las etiquetas y el contenido del tweet

    tweet_arr = []

    # if(len(re.findall("\w+", tweet)) > 0):
    #     coincidences = re.findall("\w+", tweet)
    #     for i in range(len(coincidences)):
    #         coincidences[i] = re.sub(r'\s','',coincidences[i])
    #     tweet_arr += coincidences
    #     tweet = re.sub(r'\w+','',tweet)
    #
    # if(len(re.findall("\W+", tweet)) > 0):
    #     coincidences = re.findall("\W+", tweet)
    #     for i in range(len(coincidences)):
    #         coincidences[i] = re.sub(r'\s','',coincidences[i])
    #     tweet_arr += coincidences
    #     tweet = re.sub(r'\W+','',tweet)

    # Buscamos por medio del uso de expresiones regulares todas aquellas
    # cadenas que cacen con hastags.
    if(len(re.findall("#\w+", tweet)) > 0):
        coincidences = re.findall("#\w+", tweet)
        for i in range(len(coincidences)):
            coincidences[i] = re.sub(r'\s','',coincidences[i])
        tweet_arr += coincidences
        tweet = re.sub(r'#\w+','',tweet)

    # Buscamos por medio del uso de expresiones regulares todas aquellas
    # cadenas que cacen con emoticonos.
    if(len(re.findall("(\:\w+\:|\<[\/\\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", tweet)) > 0):
        coincidences = re.findall("(\:\w+\:|\<[\/\\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", tweet)
        for i in range(len(coincidences)):
            coincidences[i] = re.sub(r'\s','',coincidences[i])
        tweet_arr += coincidences
        tweet = re.sub(r'(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)','',tweet)

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

    return tweet_arr

def processTweet2(tweet):

    # tweet = re.sub(r'@\w+','',tweet)      # Se eliminan las menciones
    # tweet = re.sub(r'#\w+','',tweet)      # Se eliminan los hashtag.
    # tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',tweet) # Se eliminan las URLs
    tweet = re.sub(r'\"','',tweet)       # Se eliminan las comillas
    tweet = re.sub(r'(?:\d+[a-z]|[a-z]+\d)[a-z\d]*','',tweet) # Se eliminan todas aquellas strings que contengan numeros.

    tweet_arr = []

    # Buscamos por medio del uso de expresiones regulares todas aquellas
    # cadenas que cacen con emoticonos.
    if(len(re.findall("(\:\w+\:|\<[\/\\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", tweet)) > 0):
        coincidences = re.findall("(\:\w+\:|\<[\/\\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", tweet)
        for i in range(len(coincidences)):
            coincidences[i] = re.sub(r'\s','',coincidences[i])
        tweet_arr += coincidences
        tweet = re.sub(r'(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)','',tweet)

    tweet = re.sub(r'[0-9]+','',tweet)   # Se eliminan los numeros

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

            # Se pasan todas las palabras a minusculas.
    for i in range(len(tweet_arr)):
        tweet_arr[i] = tweet_arr[i].lower()

    return tweet_arr

# tweet_arr = processTweet("Thank you <3")
# for word in tweet_arr:
#     print(word)
