import json
from textblob import TextBlob

with open('/Users/air/twitter_analysis_by_hatedetector2000/Data/data_10_11_2020.json') as json_data:
    data_dict = json.load(json_data)
import json


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
            trucvoulu.append(b)
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



def analyse_polarite_tweet(tweet):
    #tweetconv=TextBlob(tweet) #tweet doit etre en str
    return tweet.sentiment.polarity

def analyse_ensemble_de_tweet(tweetsanalyse,n):
    Tpos,Tneu,Tneg=0,0,0

#on imagine que l'algo fonctionne pour une data type celle importer dans les premieres lignes
    for k in range (n): #n nb de tweet analysees
        tweet=tweetsanalyse[k] #j'imagine en entree on prends une liste de tweet concernee
        if analyse_polarite_tweet(tweet)<=(-0.3):
            Tneg+=1
        if analyse_polarite_tweet(tweet)>=(0.3):
            Tpos+=1
        else:
            Tneu+=1
    return Tneg,Tneu,Tpos

def pourcentage_opinion_tweet(tweetsanalys,n): #n est le nb de tweet analysee
    Tneg,Tneu,Tpos=analyse_ensemble_de_tweet(tweetsanalys,n)
    return Tneg/n,Tneu/n,Tpos/n


def trad(tweet):
    tweetanalysee=TextBlob(str(tweet))
    if tweetanalysee.detect_language()!= 'en':
        return tweetanalysee.translate(to='en')
    else:
        return TextBlob(tweet)

def opinioncandidat(candidat):
    #on va faire appel deja aux tweets concernant le candidat, j'utilise pour cela la fonction ecrite hier
    #dans un premier tps on va analyser uniquement les tweets sans prendre en comptes le facteur retweets
    Listetweet=[]
    for k in range (len(tweetanalyseconteucomplet(candidat,0))): #lesRT ne sont pas pris en compte
        Listetweet.append(trad(str(tweetanalyseconteucomplet(candidat,0)[k])))
    print(Listetweet)
        #arriver ici on a une liste de textblob de tuple (Nb-de-RT,Tweet_traduit_en_anglais)

    return pourcentage_opinion_tweet(Listetweet,len(tweetanalyseconteucomplet(candidat,0)))





