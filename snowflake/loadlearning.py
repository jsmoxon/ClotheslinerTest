project_home="/Users/jmoxon/Clothesliner/ClotheslinerTest/snowflake/"
csv_home="/Users/jmoxon/needsupply_new.csv"

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
    pant.back_rise=row[8]
    #pant.hips=row[5]
    pant.inseam=row[3]
    pant.thigh=row[6]
    pant.knee=row[7]
    pant.outseam=row[9]
    pant.cuff=row[5]
    pant.designer_waist=row[10]
    pant.designer_inseam=row[11]
    pant.picURL=row[12]
    pant.url_link=row[13]
    pant.save()


