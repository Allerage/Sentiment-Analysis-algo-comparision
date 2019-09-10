import requests
from bs4 import BeautifulSoup
url =requests.get("https://play.google.com/store/apps/details?id=com.tencent.ig&hl=en_IN&showAllReviews=true").text
soup=BeautifulSoup(url,"lxml")

review=soup.find("div",id='fk8dgd')
print(review)

