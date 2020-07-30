# environment day speech is used for the demo  
'''
As today, the whole school has been assembled here for this beautiful occasion of World Environment Day that is celebrated on 5th June every year; I would like to say a few words dedicated to the environment.

The environment is the surroundings made from five elements namely- Air, Water, Land, Sky, and Fire for us to flourish. It has been always said that only earth has the most favourable climatic conditions that help us to survive. We should be very grateful towards the earth that we have been provided with such a great environment that has everything in its nature which helps us to thrive. But day by day we are ruining it on the highest pitch that will eventually lead us towards our destruction.

We should understand the importance of the natural environment and try to deduce our non-eco-friendly activities and imperatively plant as many trees as we can and save water that is the two biggest issues.

Thank you and have a nice day!


'''

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from string import punctuation 

#2.Inputing tha data and storing in a variable
raw_data= input('Enter paragraph here: ')

#for demo above speech can given as input


#normalising the input
#removing number,special characters and extra spaces
data2 = re.sub(r'\[[0-9]*\]', ' ',raw_data)
data3 = re.sub(r'\s+', ' ', data2)
data4 = re.sub('[^a-zA-Z]', ' ', data3)
data5 = re.sub(r'\s+', ' ', data4)
data5

 #forming senence tokenization
sentence_list1 = nltk.sent_tokenize(data3)


#word tokenization and removing stop words
stop_words=set(stopwords.words('english'))#stop words in english
wordstokenize=word_tokenize(data5)

#creating an empty ditionary
filtered_output={}

#inserting tokeniaed words and their count to dictionary
for w in wordstokenize:
    if w not in stop_words:
        if w not in filtered_output.keys():
            filtered_output[w] = 1
        else:
            filtered_output[w] += 1

            
import math
from textblob import TextBlob as tb

#creating tf value
def tf(word, doc):
    return doc.words.count(word)/len(doc.words)

def reference(word, docs):
    return sum(1 for doc in docs if word in docs.words)
#creating idf value
def idf(words, docs):
    return math.log(len(docs)/(1+reference(words,doc)))

#creating tfidf value
def tfidf(word,doc,docs):
    return tf(word,doc)*idf(word,docs)
data6=' '.join([word for word in wordstokenize if word not in stop_words])
doc1=tb(data6)

#creating list of document
docs=[doc1]

#creating the tf-idf dictionary.
for i, doc in enumerate(docs):
    scores={word: tfidf(word, doc, docs) for word in doc.words}
#to find sentence score
sentence_scores1 = {}   

for sentence in sentence_list1:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in scores.keys():
            if len(sentence.split(' '))<30:
                if sentence not in sentence_scores1.keys():
                    sentence_scores1[sentence] = scores[word]
                else:
                    sentence_scores1[sentence] =sentence_scores1[sentence]+ scores[word]
#print(sentence_scores1)
#getting the most important sentence from then setence_score1 dictionary.
summary = min(sentence_scores1, key=sentence_scores1.get)
print('-'*100)
print('SUMMARY:')
print(summary)
print('='*100)
