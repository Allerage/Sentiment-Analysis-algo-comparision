from bs4 import BeautifulSoup
import requests
import csv
l=["""https://www.amazon.in/Apple-iPhone-7-32GB-Black/product-reviews/B01LZKSVRB/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2&filterByStar=positive""",
   """https://www.amazon.in/Apple-iPhone-7-32GB-Black/product-reviews/B01LZKSVRB/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber=3&filterByStar=positive""",
   """https://www.amazon.in/Apple-iPhone-7-32GB-Black/product-reviews/B01LZKSVRB/ref=cm_cr_getr_d_paging_btm_next_4?ie=UTF8&reviewerType=all_reviews&pageNumber=4&filterByStar=positive""",
   """https://www.amazon.in/Apple-iPhone-7-32GB-Black/product-reviews/B01LZKSVRB/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber=5&filterByStar=positive"""
]
rs=open("amazonreview.csv","w")
writer=csv.writer(rs)
writer.writerow(["Review","Type"])
rs.close()
for i in l:
    print(i)
    m = requests.get(i).text
    soup = BeautifulSoup(m, "lxml")
    li = []
    for a in soup.find_all('div', {'class': 'a-section celwidget'}):
        n = a.find("span", class_="a-size-base review-text review-text-content").text
        print(n)
        with open("amazonreview.csv",mode="a")as az:
            writer=csv.writer(az)
            writer.writerow([n,"Positive"])






