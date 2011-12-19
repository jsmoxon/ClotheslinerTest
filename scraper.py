from BeautifulSoup import BeautifulSoup
import re, urllib2

i = urllib2.urlopen("http://fourhorsemen.ca/shop/category/categories/pants/")
content = i.read()
pattern = r'<h4 class="name"><a href="(.+)>'
for link in re.findall(pattern,content):
#    open_link = urllib2.urlopen(link)
 #   cont = open_link.read()
  #  pat = r'<h3 class="productname">"(.+)>'
   # print re.findall(pat,cont)
    print link

#soup = BeautifulSoup(i)

#print soup.h4
