project_home="/Users/jmoxon/Production/heroku-template-django/snowflake/"
csv_home="/Users/jmoxon/Production/heroku-template-django/snowflake/mrporter.csv"


import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')

for row in dataReader:
    designer = Designer.objects.get(name = row[5])
    style = Style.objects.get(name = row[4])
    pant=Pant()
    pant.designer= designer
    pant.style = style
    pant.waist=row[8]
    pant.front_rise=row[9]
    #pant.back_rise=row[7]
    #pant.hips=row[8]
    pant.inseam=row[10]
    #pant.thigh=row[10]
    #pant.knee=row[11]
    pant.outseam=row[11]
    pant.cuff=row[12]
    pant.designer_waist=row[6]
    pant.designer_inseam=row[7]
    pant.picURL=row[1]
    pant.url_link=row[2]
    pant.save() 
