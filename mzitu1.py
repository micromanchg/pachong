from bs4 import BeautifulSoup
import os
from download import repuest

####小白爬虫第二弹之健壮的小爬虫
class mzitu():
    def all_url(self,url):
        html=repuest.get(url,3)
        all_a=BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
        for a in all_a:
            title=a.get_text()
            print(u'开始保存标题为：',title)
            path=str(title).replace('?','_')
            self.mkdir(path)
            os.chdir('/home/chg/data/mz//'+path)
            href=a['href']
            self.html(href)

    def html(self,href):
        html=repuest.get(href,3)
        max_span=BeautifulSoup(html.text,'lxml').find_all('span')[10].get_text()
        for page in range(1,int(max_span)+1):
            page_url=href+'/'+str(page)
            self.img(page_url)

    def img(self,page_url):
        img_html=repuest.get(page_url,3)
        img_url=BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self,img_url):
        name=img_url[-9:-4]
        print(u'开始保存图片：',img_url)
        img=repuest.get(img_url,3)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    def mkdir(self,path):
        path=path.strip()
        isExists=os.path.exists(os.path.join('/home/chg/data/mz//'+path))
        if not isExists:
            print(u'建了一个名字叫做：',path,u'的文件夹')
            os.makedirs(os.path.join('/home/chg/data/mz//'+path))
            return True
        else:
            print(u'名字叫做',path,u'的文件夹已存在！')
            return False


Mzitu=mzitu()
Mzitu.all_url("http://www.mzitu.com/all")