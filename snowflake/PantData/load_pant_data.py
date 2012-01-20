project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jackmoxon/ClotheslinerTest/snowflake/PantData/need_supply_clean.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    designer = Designer.objects.get(name = row[1])
    style = Style.objects.get(name = row[2])
    pant=Pant()
    pant.designer= designer
    pant.style = style
    pant.url = row[0]
    pant.retailer1_price = row[3]
    pant.designer_waist = row[6]
    pant.designer_inseam = row[7]
    pant.waist = row[8]
    pant.front_rise = row[9]
    pant.inseam = row[10]
    pant.knee = row[11]
    pant.cuff = row[12]
    pant.thigh = row[13]
    pant.back_rise = row[14]
    pant.outseam = row[15]
    pant.hip = row[16]
    pant.retailer1_name = row[19]
    pant.retailer1_shipping = row[20]
    pant.retailer1_returns = row[21]
    pant.retailer1_url = row[24]
    pant.retailer_description = row[25]
    pant.save()


