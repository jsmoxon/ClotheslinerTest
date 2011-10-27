project_home="/Users/jmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jmoxon/needsupply_denim.csv"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    designer = Designer.objects.get(name = row[1])
    style = Style.objects.get(name = row[0])
    pant=Pant()
    pant.designer= designer
    pant.style = style
    pant.waist=row[2]
    pant.front_rise=row[4]
    #pant.back_rise=row[9]
    #pant.hips=row[5]
    pant.inseam=row[3]
    pant.thigh=row[6]
    pant.knee=row[7]
    #pant.outseam=row[14]
    pant.cuff=row[5]
    pant.designer_waist=row[8]
    pant.designer_inseam=row[9]
    pant.picURL=row[11]
    pant.url_link=row[12]
    pant.save()


