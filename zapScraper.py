from BeautifulSoup import BeautifulSoup
import re, urllib2, csv

pantWriter = csv.writer(open('zappos.csv', 'wb'), delimiter=",")

link_list = "http://www.zappos.com/mens-pants-clothing~1z"
x = urllib2.urlopen(link_list)
soup = BeautifulSoup(x)
list = soup.findAll("div", {"id": "searchResults"})
parse = BeautifulSoup(str(list))
url_search=parse.findAll("a")
prod_url_list = []
for item in url_search:
    prod_url_list.append(item['href'])
for pant in prod_url_list:
    open = urllib2.urlopen("http://zappos.com"+pant)
    y = BeautifulSoup(open)
    sku = y.find("span", {"class":"sku"})
    soup_sku = BeautifulSoup(str(sku))
    final_sku = soup_sku.span.contents[0][6:]
    #now use api
    api_url = "http://api.zappos.com/Product/"+final_sku+"?includes=[%22measurements%22]&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de"
    z = urllib2.urlopen(api_url)
    print 
