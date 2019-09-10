import pickle

posf=open("positive.txt").read().splitlines()
negf=open("negative.txt").read().splitlines()
with open("positive.pkl","rb") as p:
    p=pickle.load(p)
with open("negative.pkl","rb") as n:
    n=pickle.load(n)
print(len(posf))
print(len(posf))
print(len(posf))
print(len(posf))






