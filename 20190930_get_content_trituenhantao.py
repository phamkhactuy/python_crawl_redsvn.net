import urllib
from bs4 import BeautifulSoup
url = "https://trituenhantao.info/quan-ly-phien-ban-database-voi-liquibase/"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
print(con)
soup = BeautifulSoup(con, 'html.parser')
type(soup)
title = soup.title
print(title)
text = soup.get_text()
all_links = soup.find_all("p")
#for link in all_links:
    #print(link)
pk=soup.findAll("div", {"class": "entry-content"})
for l in pk:
    print(l)
