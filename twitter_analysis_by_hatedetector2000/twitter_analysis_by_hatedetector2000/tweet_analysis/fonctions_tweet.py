
#%% Fonction qui permet d'extraire le tweet d'un ensemble de de tweets ayant le plus
#retweet
def morert(data):
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))


#%%Fonction qui permet d'extraire le tweet d'un ensemble de de tweets ayant le plus
#like

def morelike(data):
    likes_max  = np.max(data['Likes'])
    like  = data[data.Likes == likes_max].index[0]

    # Max Likes:
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][like]))
    print("Number of retweets: {}".format(likes_max))
    print("{} characters.\n".format(data['len'][like]))


