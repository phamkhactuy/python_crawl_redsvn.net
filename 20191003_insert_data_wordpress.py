# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import MySQLdb
db = MySQLdb.connect(host="127.0.0.1", port=3309, user="root", passwd="", db="pktuy",charset='utf8')
c = db.cursor()
url = "https://trituenhantao.info/blog-cong-nghe-thong-tin/"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
print(con)
soup = BeautifulSoup(con, 'html.parser')
type(soup)
title = soup.title
print(title.get_text())
text = soup.get_text()
all_links = soup.find_all("p")
a1="https://trituenhantao.info/posts"
c.execute("SELECT id,post_title FROM wp_posts")
a2=0
for id, posttitle in c:
    if a2<id:
        a2=id
print('-----------------------')
pk=soup.findAll("div", {"class": "entry-content"})
a=a2
for l in pk:
    a=a+1
    print(l)
    l1=l
    sql=f"INSERT INTO `wp_posts`(`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_name`, `guid`) VALUES ({a},'admin',now(),now(),'{l1}','111111{a}',{a},'http://localhost/resdvn/?p={a}')"
    c.execute(sql)
    db.commit()
    
