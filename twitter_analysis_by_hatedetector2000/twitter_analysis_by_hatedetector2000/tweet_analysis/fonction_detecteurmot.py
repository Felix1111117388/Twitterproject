import json

with open('/Users/air/twitter_analysis_by_hatedetector2000/Data/data_10_11_2020.json') as json_data:
    data_dict = json.load(json_data)



def list_retweet (L):
    listr=[]
    for k in range (len(L)):
        dicok=L[k]
        listr.append(dicok['favorite_count'])
    return listr


def tweetanalyseconteu(mot,nbRTmin):
    n=nbRTmin
    L=[]
    for k in range (15):
        tweet = data_dict['tweet_textual_content'][str(k)]
        listetweet=tweet.split()
        for mottwe in listetweet:
            if len(mottwe)>=len(mot):
                    if mottwe[0:len(mot)+1] == mot:

                        L.append(k)
#L contient toutes les cles contenant les tweets ayant a l'interieur le mot voulu
    trucvoulu=[]
    for k in L:
        if data_dict['RTs'][str(k)] >= nbRTmin:
            a,b=data_dict['RTs'][str(k)],data_dict['tweet_textual_content'][str(k)]
            trucvoulu.append((a,b))
    return trucvoulu





def tweetanalyseconteucomplet(mot,nbRTmin):
    mot = mot.lower()
#ca permet de mettre le mot chercher en minuscule pour eviter les problemes lies aux comaparisons futurs
    n=nbRTmin
    L=[]
    for k in range (15):
        tweet = data_dict['tweet_textual_content'][str(k)]

        listetweet=tweet.lower().split()
#on separe chaque tweet en liste de mot tout en les rendant en minuscule pour ne pas avoir de probleme de comparaison
        for mottwe in listetweet:
            if len(mottwe)>=len(mot):
                    for i in range (len(mottwe)):
                        for j in range (len(mottwe)):
                            if mottwe[i:j+1]==mot:
                                L.append(k)

#L contient toutes les cles contenant les tweets ayant a l'interieur le mot voulu
    trucvoulu=[]
    for k in L:
        if data_dict['RTs'][str(k)] >= nbRTmin:
            a,b=data_dict['RTs'][str(k)],data_dict['tweet_textual_content'][str(k)]
            trucvoulu.append((a,b))
    return trucvoulu




























