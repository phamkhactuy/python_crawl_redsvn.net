# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
###
import MySQLdb
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="Quynh307", db="PKTUY",charset='utf8')
c = db.cursor()
a1="https://trituenhantao.info/posts"
# https://tukyonline.com/blog
#http://www.hubertiming.com/results/2017GPTR10K
#http://redsvn.net/loat-anh-quy-gia-it-nguoi-biet-ve-viet-nam-nam-1926/
#https://mariadb.com/kb/en/library/create-table/
url = "http://redsvn.net/loat-anh-quy-gia-it-nguoi-biet-ve-viet-nam-nam-1926/"

#for link in all_links:
    #print(link.get("href"))
    #a1=link.get("href")
    #sql=f"insert into tukyonline values('{a1}',NOW())"
    #c.execute(sql)
db1 = MySQLdb.connect(host="127.0.0.1", port=3309, user="root", passwd="", db="pktuy",charset='utf8')
c1 = db1.cursor()
c1.execute("SELECT id,post_title FROM wp_posts")
a2=0
for id, posttitle in c1:
    if a2<id:
        a2=id
c.execute("SELECT url,stt FROM redsvn where stt is null  order by url LIMIT 100")
# Loop through the results
for url, datcre in c:
    print(f'------------------------------')
    print(f'First name: {url}, Last name: {datcre}')
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title
    ti=title.get_text()
    print(ti)
    text = soup.get_text()
    pk=soup.findAll("div", {"class": "entry-content"})
    a2=a2+1
    a=a2
    for l in pk:
        a=a+1
        #print(l)
        l=f"{l}"
        ti=f"{ti}"
        ti=ti.replace("\'"," ")
        ti=ti.replace("\'”"," ")
        l1=l.replace("\'script\'","script")
        l1=l1.replace("\'facebook-jssdk\'","facebook-jssdk")
        sql1=f"INSERT INTO `wp_posts`(`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_name`, `guid`) VALUES ({a},'admin',now(),now(),'{l1}',{a},{a},'http://localhost/resdvn/?p={a}')"
        c1.execute(sql1)
        db1.commit()
        ti=ti.replace(" - Redsvn.net","")
        s1=url.replace("http://redsvn.net/","")
        s1=s1.replace("/","")
        sql2=f"UPDATE `wp_posts` SET `post_title` = '{ti}',post_name='{s1}' WHERE `wp_posts`.`ID` = {a}";        
        c1.execute(sql2)
        db1.commit()
    sql3=f"UPDATE `redsvn` SET `stt` = '1' WHERE url = '{url}'";        
    c.execute(sql3)
    db.commit()
# Print output of the query
print(c.fetchone())
