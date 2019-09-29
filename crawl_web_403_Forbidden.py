import urllib
from bs4 import BeautifulSoup
url = "https://thefullsnack.com/"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
print(con)
soup = BeautifulSoup(con, 'html.parser')
type(soup)
title = soup.title
print(title)
text = soup.get_text()
soup.find_all('a')
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
    a1=link.get("href")
