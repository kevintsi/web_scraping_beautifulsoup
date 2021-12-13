import requests
from bs4 import BeautifulSoup
import pandas as pd

request_text = requests.get("https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020")

print(request_text)

soup = BeautifulSoup(request_text.content, 'html.parser')

#print(soup.prettify())

print("Il y a {} balises table ".format(len(soup.find_all("table"))))

#print(soup.find("table"))

#print(soup.find_all("table",class_="wikitable", limit=1))

table = soup.find("table",class_="DebutCarte")

#print(table.find("tbody").find_all("a"))

clubs = table.find_all("a")[:5]

df = pd.DataFrame(columns=["Club","URL"])

for club in clubs:
    if club.find("img"):
        continue

    df = df.append({"URL" : club.get("href"), "Club" : club.getText()}, ignore_index=True)
    print("URL : {0} , Nom : {1}".format(club.get("href"), club.getText()))
    print("----------")

print(df)
df.to_csv("./Club_Web_Scraping.csv")
df.to_excel("./Club_Web_Scraping.xlsx")