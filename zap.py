from BeautifulSoup import BeautifulSoup
import re, urllib2, csv
import simplejson as json

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
    prodURL = "http://zappos.com"+pant
    open = urllib2.urlopen(prodURL)
    y = BeautifulSoup(open)
    sku = y.find("span", {"class":"sku"})
    soup_sku = BeautifulSoup(str(sku))
    final_sku = soup_sku.span.contents[0][6:]
    #now use api
    api_url = "http://api.zappos.com/Product/"+final_sku+"?includes=[%22measurements%22]&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de"
    z = urllib2.urlopen(api_url)
    jsonCity = json.load(z)
    waist =  jsonCity['product'][0]['measurements'][0]['value']
    outseam =  jsonCity['product'][0]['measurements'][1]['value']
    inseam =  jsonCity['product'][0]['measurements'][2]['value']
    front =  jsonCity['product'][0]['measurements'][3]['value']
    back =  jsonCity['product'][0]['measurements'][4]['value']
    leg =  jsonCity['product'][0]['measurements'][5]['value']
    price = y.find("span", {'id':'price'}).contents[0]
    brand = y.find("a", {'class':'to-brand'}).contents[0]
    style = y.find('span', {'class':'prName'}).contents[1]
    picURL = y.find('img', {'id':'detailImage'})['src']
    meas_taken = y.find(text=re.compile('Product measurements'))
    knee = ""
    thigh=""
#    pantWriter.writerow([prodURL, brand, style, price, picURL, meas_taken, waist, front, inseam, knee, cuff, thigh, back, outseam])
    print waist


