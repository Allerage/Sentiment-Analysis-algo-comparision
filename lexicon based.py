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
m=["""This game use to be great. If I spend $15 to get a battle pass I expect to be able to get to level 100 without paying more money to get there or expected to play every single day (not every person can play every day of the week, some may only be able to play 3 times a week) why should they have to pay more money to complete level 100? absolutely disgusting this game has turned more about greedy developers. And what's the go with play this emote for challenges? im an adult not a child!""","""its fun, just lags sometimes but that prob my internet. It would be really fun though if there was a shop in the future to choose a companion, it could be a different breed of dogs or maybe even different animals. Then you can give armor to your dog in game if you find some, and upgrade your companion? That companions purpose would be to help you in game.""","""I hate this game"""]
positive_words=[]
negative_words=[]
nc=open("review.csv","w")
nw=csv.writer(nc)
nw.writerow(["review","Positive ","Negative","Score","Type"])
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
        print(i+" review under consideration")
        w=word_tokenize(i)

        fs = []
        for word in w:
            if word  not in sw and word not in pun:
                fs.append(word.lower().replace(".",""))
        pl.append(fs)
        n=bag_of_word(pl)
        print(n)
        lex=lexicon(n,w)
        print(lex)

        resultframe= {

            "Review": comment_review,
            "Result": "Positive",
            "Lexscore": lex[2],
            "Positive Words": lex[0],
            "Negative Words": lex[1]

        }


        if(lex[2]>0):
            #tocsv(comment_review,"Positive",lex,positive_words,negative_words)
            if(len(lex[0])>len(lex[1])):
                n=abs(len(lex[0])-len(lex[1]))
                for i in range (n):
                    lex[1].append("")
                print(str(len(lex[1])-len(lex[0]))+ "is the final length" )

            with open("review.csv", mode="a") as negat:
                writer = csv.writer(negat)
                writer.writerow([comment_review, lex[0], lex[1], lex[2], "Positive"])


        if(lex[2]<=0):
            print("!!!")
            if (len(lex[0]) < len(lex[1])):
                n = abs(len(lex[0]) - len(lex[1]))
                for i in range(n):
                    lex[0].append("")
                print(str(len(lex[1]) - len(lex[0])) + "is the final length")




            with open("review.csv", mode="a") as negat:
                writer=csv.writer(negat)
                writer.writerow([comment_review,lex[0],lex[1],lex[2],"Negative"])








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
    print(po ,end=" ")
    print("list of positive words ", )
    for i in token:
        try:
            if i not in neg:
                pass
            else:

                ne.append(i)
        except:
            pass
    print(ne ,end=" ")
    print("list of negative words")
    lexscore=(len(po)-len(ne))/len(token)
    print(lexscore)
    positive_words.append(po)
    negative_words.append(ne)
    srl=[]
    srl.append(po)
    srl.append(ne)
    srl.append(lexscore)


    return srl













def bag_of_word(pl):
    bgl=pl
    print(bgl)
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