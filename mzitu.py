import requests
from bs4 import BeautifulSoup
import os



headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url="http://mzitu.com/all"
start_html=requests.get(all_url,headers=headers)
#print(start_html.text)
Soup=BeautifulSoup(start_html.text,'lxml')
#li_list=Soup.find_all('li')
#for li in li_list:
#    print(li)
all_a=Soup.find('div',class_='all').find_all('a')
for a in all_a:

    title=a.get_text()
    path = str(title).strip()
    os.makedirs(os.path.join('/home/chg/data/mz',path))
    os.chdir('/home/chg/data/mz//'+path)
    href=a['href']
    #print(title,href)
    html=requests.get(href,headers=headers)
    html_soup=BeautifulSoup(html.text,'lxml')
    max_span=html_soup.find_all('span')[10].get_text()
    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)
        img_html=requests.get(page_url,headers=headers)
        img_soup=BeautifulSoup(img_html.text,'lxml')
        img_url=img_soup.find('div',class_='main-image').find('img')['src']
        #print(img_url)
        name=img_url[-9:-4]
        img=requests.get(img_url,headers=headers)
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()
