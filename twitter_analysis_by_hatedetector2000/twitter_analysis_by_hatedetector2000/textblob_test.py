from textblob import TextBlob
wiki = TextBlob('Python is a high-level, general-purpose programming language.')

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")



zen = TextBlob("Beautiful is better than ugly. "
             "Explicit is better than implicit. "
               "Simple is better than complex.")

sentence = TextBlob('Use 4 spaces per indentation level.')

from textblob import Word
from textblob.wordnet import VERB




import json
with open(r"C:\Users\White\Documents\CW\hate_detector2000\twitter_analysis_by_hatedetector2000\Data\data_10_11_2020.json",encoding="utf8") as json_file:
    data = json.load(json_file)
    
def mots_uniques_lemma(d):
    fin=[]
    for k in d['tweet_textual_content']:
        wlist=[]
        a = TextBlob(d['tweet_textual_content'][k])
        for couple in a.tags:
            if couple[1] != 'DT':
                wlist.append(couple[0])
        for w in wlist:
            if w.lemmatize() not in fin:
                fin.append(w.lemmatize())
    return fin

print(mots_uniques_lemma(data))

        
