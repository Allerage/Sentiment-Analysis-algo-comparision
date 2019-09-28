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

ini=input("enter the sentence")
m=[]
#m=["""This movie is not bad""","""This is a good movie""","""This movie is bad"""]
m.append(ini)
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


        if( (len(lex[1])==2 and lex[1][0]=="not" )or (lex[2]>0) ):
            #tocsv(comment_review,"Positive",lex,positive_words,negative_words)
            if(len(lex[0])>len(lex[1])):
                n=abs(len(lex[0])-len(lex[1]))
                for i in range (n):
                    lex[1].append("")


            with open("review.csv", mode="a") as negat:
                writer = csv.writer(negat)
                writer.writerow([comment_review, lex[0], lex[1], abs(lex[2]), "Positive"])
            for i,j in resultframe.items():
                print("{}->{}".format(i,j))


            print("{}->{}".format("Result","  Positive"))
            print("--------------------------------------------------------------")




        elif(lex[2]<=0):
            re="Negative"
            if(len(lex[0])==len(lex[1])):
                re="Netural"



            if (len(lex[0]) < len(lex[1])):
                n = abs(len(lex[0]) - len(lex[1]))
                for i in range(n):
                    lex[0].append("")





            with open("review.csv", mode="a") as negat:
                writer=csv.writer(negat)
                writer.writerow([comment_review,lex[0],lex[1],lex[2],re])
            for i, j in resultframe.items():
                print("{}->{}".format(i, j))

            print("{}->{}".format("Result", re))
            print("--------------------------------------------------------------")

        else:

            pass







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
        neg.append("not")
    return neg

data_preprocessing()