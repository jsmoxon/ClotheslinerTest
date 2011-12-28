from BeautifulSoup import BeautifulSoup
import re, urllib2, csv

pantWriter = csv.writer(open('need.csv', 'wb'), delimiter=",")

link_list = ("http://needsupply.com/mens/bottoms/pants", "http://needsupply.com/mens/bottoms/pants?p=2", "http://needsupply.com/mens/bottoms/pants?p=3", "http://needsupply.com/mens/denim", "http://needsupply.com/mens/denim?p=2", "http://needsupply.com/mens/denim?p=3", "http://needsupply.com/mens/denim?p=4") 
for link in link_list:
    i = urllib2.urlopen(link)
    soup = BeautifulSoup(i)
    list = soup.findAll("div", {"class":"product"})
    for item in list: 
        url = item.a['href']
        designer = item.h4.a.contents[0]
        style = item.h3.a.contents[0]
        dash = item.find('span')
        price = dash.findNext('span').contents[0]
        image = item.img['src']
        #get measurement data
        r = urllib2.urlopen(url)
        psoup = BeautifulSoup(r)
        description = str(psoup.findAll("div", {"class":"description"}))
        desc = BeautifulSoup(description)
        waist = desc.find(text=re.compile('" waist'))
        waistband = desc.find(text=re.compile('waistband'))
        front_rise = str(desc.find(text=re.compile(" front rise")))[2:]
        inseam = str(desc.find(text=re.compile('" inseam')))[2:]
        thigh = str(desc.find(text=re.compile('thigh')))[2:]
        knee = str(desc.find(text=re.compile('knee')))[2:]
        cuff = str(desc.find(text=re.compile('leg opening')))[2:]
        back_rise = str(desc.find(text=re.compile('back rise')))[2:]
        measurement = desc.find(text=re.compile('Measurements')) or desc.find(text=re.compile('Measured'))
        pantWriter.writerow([url, designer, style, price, image, measurement, waist, waistband, front_rise, inseam, knee, cuff, thigh, back_rise])
