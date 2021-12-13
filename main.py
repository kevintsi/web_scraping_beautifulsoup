import requests
from bs4 import BeautifulSoup

request_text = requests.get("https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020")

print(request_text)

soup = BeautifulSoup(request_text.content, 'html.parser')

#print(soup.prettify())

print("Il y a {} balises table ".format(len(soup.find_all("table"))))

#print(soup.find("table"))

#print(soup.find_all("table",class_="wikitable", limit=1))

team_table = soup.find_all("table",class_="wikitable")[0]

#print(team_table.find("tbody").find_all("tr"))

trs = team_table.find("tbody").find_all("tr")[:5]

for tr in trs:
    print(tr.find("a"))
    print("---------------------")
