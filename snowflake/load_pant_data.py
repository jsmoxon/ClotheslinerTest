project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jackmoxon/ClotheslinerTest/upload.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

style_list = Style.objects.all()
style_list_two = []
designer_objects = Designer.objects.all()
designer_list = []

for obj in style_list:
    style_list_two += [obj.name]

for des in designer_objects:
    designer_list += [des.name]

for row in dataReader:
    item=Style()
    if row[2] not in style_list_two:
        item.name = row[2]
        item.save()
        style_list_two.append(row[2])
    else:
        print row[2]
    designer=Designer()
    if row[1] not in designer_list:
        designer.name = row[1]
        designer.save()
        designer_list.append(row[1])
    else:
        print row[1]

pantReader = csv.reader(open(csv_home, "rU"), delimiter=',')

dup_list = []
for row in pantReader:
    if row[2] not in dup_list:
        designer = Designer.objects.get(name = row[1])
        style = Style.objects.get(name = row[2])
        pant = Pant()
        pant.designer= designer
        pant.style = style
        pant.url_link = row[0]
        pant.picURL = row[4]
        pant.designer_waist = row[6]
        pant.designer_inseam = row[7]
        pant.waist = row[8]
        pant.front_rise = row[9]
        pant.inseam = row[10]
        if row[11] !="":
            pant.knee = row[11]
        else:
            pass
        pant.cuff = row[12]
        if row[13] != "":
            pant.thigh = row[13]
        else:
            pass
        if row[14] != "":
            pant.back_rise = row[14]
        else:
            pass
        if row[15] !="":
            pant.outseam = row[15]
        else:
            pass
        pant.retailer1_name = row[17]
        pant.retailer1_shipping = row[18]
        pant.retailer1_returns = row[19]
        pant.retailer1_location = row[20]
        pant.retailer1_price = row[21]
        pant.retailer1_url = row[22]
        pant.retailer1_description = row[23]
        pant.save()
        dup_list.append(row[2])
    else: 
        pass

