import nltk
import string
import pandas as pd
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import pickle
from lcsv import tocsv
import csv
from bs4 import BeautifulSoup
import requests
import re
"""def data_collector():#amazon review scraper
    m = requests.get("https://www.amazon.in/Apple-iPhone-7-32GB-Black/product-reviews/B01LZKSVRB/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews").text
    soup = BeautifulSoup(m, "lxml")
    li = []
    for a in soup.find_all('div', {'class': 'a-section celwidget'}):
        n = a.find("span", class_="a-size-base review-text review-text-content").text
        li.append(n.lower())
    print(li)
    return li"""
m=["""I have ordered many things from an Amazon, it was a wonderful experience which gives by amazon. I love to use for further bookings.I would recommended people to use amazon""","""Very bad experience ..I order a phone and received soap ..and now they don't receive or replace ..I am very disappointed with your service I lost my money

""","""and why there are so many reiterated negative reviews. I have not spent a single dollar on this game and this game is very enjoyable and fun to play. I fail to understand why all these other parents are just babbling on about how this game wants your money. Enjoyable and fun, although it does require a little bit of investment if you want to get very good in this game"""]
positive_words=[]
negative_words=[]
nc=open("review.csv","w")
nw=csv.writer(nc)
nw.writerow(["Review","Positive ","Negative","Score","Type"])
nc.close()

def data_preprocessing():#applying data cleaning
    positive_reviews=[]
    negative_reviews=[]

    pun=set(string.punctuation)
    sw=set(stopwords.words('english'))
    pl=[]




    for i in  m:
        rl=[]

        comment_review=i

        w=word_tokenize(i)

        fs = []
        for word in w:
            if word  not in sw and word not in pun:
                fs.append(word.lower().replace(".",""))
        pl.append(fs)
        n=bag_of_word(pl)

        lex=lexicon(n,w)


        resultframe= {

            "Review": comment_review,

            "Positive Words": lex[0],
            "Negative Words": lex[1],
            "Lexscore": lex[2]

        }


        if(lex[2]>0):
            #tocsv(comment_review,"Positive",lex,positive_words,negative_words)
            if(len(lex[0])>len(lex[1])):
                n=abs(len(lex[0])-len(lex[1]))
                for i in range (n):
                    lex[1].append("")


            with open("review.csv", mode="a") as negat:
                writer = csv.writer(negat)
                writer.writerow([comment_review, lex[0], lex[1], lex[2], "Positive"])
            for i,j in resultframe.items():
                print("{}->{}".format(i,j))


            print("{}->{}".format("Result","  Positive"))
            print("--------------------------------------------------------------")



        if(lex[2]<=0):

            if (len(lex[0]) < len(lex[1])):
                n = abs(len(lex[0]) - len(lex[1]))
                for i in range(n):
                    lex[0].append("")





            with open("review.csv", mode="a") as negat:
                writer=csv.writer(negat)
                writer.writerow([comment_review,lex[0],lex[1],lex[2],"Negative"])
            for i, j in resultframe.items():
                print("{}->{}".format(i, j))

            print("{}->{}".format("Result", " Negative"))
            print("--------------------------------------------------------------")









            #tocsv(comment_review, "Negative", lex, positive_words, negative_words)






def lexicon(n,w):
    pos=loadposref()
    po = []
    ne = []



    neg=loadnegref()


    token=w
    bow=n
    for i in token:

        try:
            if i not in pos:
                pass
            else:


                po.append(i)
        except:
            pass


    for i in token:
        try:
            if i not in neg:
                pass
            else:

                ne.append(i)
        except:
            pass

    lexscore=(len(po)-len(ne))/len(token)

    positive_words.append(po)
    negative_words.append(ne)
    srl=[]
    srl.append(po)
    srl.append(ne)
    srl.append(lexscore)


    return srl


def bag_of_word(pl):
    bgl=pl

    wordfreq={}
    for a in bgl:
        for token in a:
            if token not in wordfreq.keys():
                wordfreq[token] = 1
            else:
                wordfreq[token] += 1


    return wordfreq
def loadposref():
    with open("positive.pkl","rb") as p:
        pos=pickle.load(p)
        pos.append("like")
    return pos
def loadnegref():
    with open("negative.pkl","rb") as n:
        neg=pickle.load(n)
        neg.append("n't")
    return neg

data_preprocessing()