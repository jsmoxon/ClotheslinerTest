project_home="/Users/jmoxon/Clothesliner/ClotheslinerTest/snowflake/"
csv_home="/Users/jmoxon/Clothesliner/ClotheslinerTest/snowflake/PantData/pant_stock.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    pant_object = Pant.objects.get(pk = row[0])
    pant=Pant_Stock_Item()
    pant.item = pant_object
    pant.retailer = row[1]
    pant.price = row[2]
    url_link= row[3]
    picURL = row[4]
    inventory_number = row[5]
    pant.save()


