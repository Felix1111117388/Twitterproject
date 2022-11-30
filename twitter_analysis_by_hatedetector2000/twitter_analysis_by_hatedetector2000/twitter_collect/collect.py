from connect import twitter_setup
import tweepy

def collect():
    connexion = twitter_setup()
    tweets = connexion.search_tweets("Emmanuel Macron",lang="fr",count=100)
    for tweet in tweets:
        print(tweet.text)

collect()
