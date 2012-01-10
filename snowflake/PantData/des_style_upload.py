project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jackmoxon/ClotheslinerTest/snowflake/PantData/test.csv"


import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from clothes.models import *

import csv
dataReader = csv.reader(open(csv_home, "rU"), delimiter=',')



for row in dataReader:
    item=Style()
    item.name = row[0]
    item.save()
    des = Designer()
    des.name = row[1]
    des.save()

        
