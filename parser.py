from BeautifulSoup import BeautifulSoup
import re, urllib2, csv

pantWriter = csv.writer(open('pant.csv'), delimiter=",")

i = urllib2.urlopen("http://fourhorsemen.ca/shop/category/categories/denim/")
soup = BeautifulSoup(i)
list = soup.findAll("li", {"class":"product"})
for item in list: 
    url= item.h4.a['href']
    name= item.h4.a.contents[0]
    price= item.p.contents[0]
    image= item.img['src']
    print (url, name, price, image)
