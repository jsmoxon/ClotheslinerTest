import re, urllib2, csv
import simplejson as json

pantWriter = csv.writer(open('zappos.csv', 'wb'), delimiter=",")

link_list = ["http://api.zappos.com/Search/term/mens%20pants?limit=100&page=1&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de", "http://api.zappos.com/Search/term/mens%20pants?limit=100&page=2&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=3&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=4&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=5&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=6&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=7&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=8&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=9&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=10&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=11&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de","http://api.zappos.com/Search/term/mens%20pants?limit=100&page=12&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de"]

id_list = []
for link in link_list:
    x = urllib2.urlopen(link)
    jsonCity = json.load(x)
    results = jsonCity['results']
    for result in results:
        id_list += [result['productId']]

for id in id_list:
    try:
        searchurl = "http://api.zappos.com/Product/"+id+"?includes=[%22measurements%22,%20%22styles%22]&key=cf3dffea27e37c3371ee725fa5f19bea2c23e5de"
        y = urllib2.urlopen(searchurl)
        yJson = json.load(y)   
        waist =  yJson['product'][0]['measurements'][0]['value']
        outseam =  yJson['product'][0]['measurements'][1]['value']
        inseam =  yJson['product'][0]['measurements'][2]['value']
        front =  yJson['product'][0]['measurements'][3]['value']
        picURL = yJson['product'][0]['defaultImageUrl']
        url = yJson['product'][0]['defaultProductUrl']
        designer = yJson['product'][0]['brandName']
        style = yJson['product'][0]['productName']
        try:
            price = yJson['product'][0]['styles'][0]['price']
        except: 
            price = "noting" 
        back =  yJson['product'][0]['measurements'][4]['value']
        leg =  yJson['product'][0]['measurements'][5]['value']
    except: 
        print "borken link"+id
    pantWriter.writerow([designer, style, price, picURL, url, waist, outseam, inseam, front, leg, back])
  #  style = y.find('span', {'class':'prName'}).contents[1]
  #  picURL = y.find('img', {'id':'detailImage'})['src']
  #  meas_taken = y.find(text=re.compile('Product measurements'))
  #  knee = ""
  #  thigh=""
#    pantWriter.writerow([prodURL, brand, style, price, picURL, meas_taken, waist, front, inseam, knee, cuff, thigh, back, outseam])
  #  print waist


