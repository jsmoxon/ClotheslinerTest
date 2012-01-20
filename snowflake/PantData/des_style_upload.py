project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
<<<<<<< HEAD
csv_home="/Users/jackmoxon/ClotheslinerTest/zappos.csv"
=======
csv_home="/Users/jackmoxon/ClotheslinerTest/snowflake/PantData/test.csv"
>>>>>>> cd04f8f83ca6b94d96e666034b672567432805db


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
<<<<<<< HEAD
    if row[1] not in style_list_two:
        item.name = row[1]
        item.save()
        style_list_two.append(row[1])
    else:
        print row[1]
    designer=Designer()
    if row[0] not in designer_list:
        designer.name = row[0]
        designer.save()
        designer_list.append(row[0])
    else:
        print row[0]

=======
    item.name = row[0]
    item.save()
    des = Designer()
    des.name = row[1]
    des.save()
>>>>>>> cd04f8f83ca6b94d96e666034b672567432805db

        
