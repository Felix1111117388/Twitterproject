import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import json
with open('C:/Data/CentraleSupélec/coding_weeks/projet/twitter_analysis_by_hatedetector2000/Data/data_10_11_2020.json',encoding="utf8") as json_file:
    data = json.load(json_file)


#print(data.keys())
#print(data['Date'])
#print(data['Likes'].values())

tfav = pd.Series(data=data['Likes'].values(), index=data['Date'].values())
tret = pd.Series(data=data['RTs'].values(), index=data['Date'].values())

#print(tfav)
# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)
plt.show()

'''
# Représentation des Retweets en fonction des Likes
graphe3 = pd.Series(data=data['RTs'].values(), index=data['Likes'].values())
graphe3.plot(figsize=(16,4), label="Retweets en fonctions des Likes", legend=True)
plt.show()
'''