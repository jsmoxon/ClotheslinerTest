project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jackmoxon/ClotheslinerTest/zapposClean1.csv"

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
    pant.url_link = row[6]
    pant.picURL = row[4]
    pant.retailer1_price = row[2]
    pant.designer_waist = row[4]
    pant.designer_inseam = row[5]
    if row[7] != "":
        pant.waist = row[7]
    else: 
        pass
    pant.outseam = row[8]
    pant.inseam = row[9]
    pant.front_rise = row[10]
    pant.cuff = row[11]
    pant.back_rise = row[12]
    pant.save()


