project_home="/Users/jmoxon/ClotheslinerTest/snowflake/"
csv_home="/Users/jmoxon/needsupply_denim.csv"


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


        
