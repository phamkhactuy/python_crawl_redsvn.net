import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
###
import MySQLdb
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="Quynh307", db="PKTUY")
c = db.cursor()
a1="https://trituenhantao.info/posts"
c.execute("SELECT url,datcre FROM tukyonline")
a2=0
for url, datcre in c:
    #print(f'First name: {url}, Last name: {datcre}')
    if url.startswith('http://redsvn.net'):
        a2=a2+1
        print(f'{a2}First name: {url}, Last name: {datcre}')
        url1 = url
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        type(soup)
        title = soup.title
        print(title)
        text = soup.get_text()
        soup.find_all('a')
        all_links = soup.find_all("a")
        for link in all_links:
            #print(link.get("href"))
            a1=link.get("href")
            sql=f"insert into tukyonline values('{a1}',NOW())"
            c.execute(sql)
        db.commit()


#print(c.fetchone())
