project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jackmoxon/ClotheslinerTest/zappos.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    designer = Designer.objects.get(name = row[0])
    style = Style.objects.get(name = row[1])
    pant = Pant()
    pant.designer= designer
    pant.style = style
    pant.url_link = row[4]
    pant.picURL = row[3]
    pant.retailer1_price = row[2]
    pant.designer_waist = row[5]
    pant.designer_inseam = row[7]
    pant.waist = row[5]
    pant.front_rise = row[8]
    try:
        pant.inseam = row[7]
    except:
        pant.inseam = "4.23"
#    pant.knee = row[11]
    pant.cuff = row[9]
#    pant.thigh = row[13]
    pant.back_rise = row[10]
    pant.outseam = row[6]
 #   pant.hip = row[16]
    pant.retailer1_name = row[11]
    pant.retailer1_shipping = row[12]
    pant.retailer1_returns = row[13]
    pant.retailer1_location = row[14]
#    pant.retailer1_url = row[24]
#    pant.retailer_description = row[25]
    pant.save()
    print pant.waist
