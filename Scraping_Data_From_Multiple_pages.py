import requests
import pandas as pd  
from bs4 import BeautifulSoup
NAmes=[]
Reviews=[]
price=[]
Desc=[]
for i in range(1,342):
    
    url="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=requests.get(url)
    print(r)



    soup=BeautifulSoup(r.text,"html.parser")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

    name=box.find_all("div",class_="_4rR01T")
    for i in name:
        NAme=i.text
        NAmes.append(NAme)
    # print(NAmes)
    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        p=i.text
        price.append(p)
    # print(price)
    Description=box.find_all("ul",class_="_1xgFaf")
    for i in Description:
        dec=i.text 
        Desc.append(dec)
    # print(Desc)
    view=box.find_all("div",class_="_3LWZlK")
    for i in view:
        v=i.text
        Reviews.append(v)
    # print(Reviews)

df=pd.DataFrame({"Product Name":NAmes,"Product Price":price,"Description":Desc,"Reviews":Reviews})
# print(df)
df.to_csv("mobile_From_Flip_Cart.csv")