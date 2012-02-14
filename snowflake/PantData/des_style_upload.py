project_home="/Users/jackmoxon/ClotheslinerTest/snowflake/"
<<<<<<< HEAD
<<<<<<< HEAD
csv_home="/Users/jackmoxon/ClotheslinerTest/zappos.csv"
=======
csv_home="/Users/jackmoxon/ClotheslinerTest/snowflake/PantData/test.csv"
>>>>>>> cd04f8f83ca6b94d96e666034b672567432805db
=======
csv_home="/Users/jackmoxon/ClotheslinerTest/snowflake/PantData/test.csv"
=======
csv_home="/Users/jackmoxon/ClotheslinerTest/zappos.csv"
>>>>>>> 5fb667537c08794ab1c7eaef1b8d5148f49960a5
>>>>>>> 40821969a4f630baf09fb1df441b54e5e53e7ffb


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
<<<<<<< HEAD
#    item=Style()
 #   item.name = row[0]
  #  item.save()
=======
    item=Style()
<<<<<<< HEAD
<<<<<<< HEAD
=======
    item.name = row[0]
    item.save()
    des = Designer()
    des.name = row[1]
    des.save()
=======
>>>>>>> 40821969a4f630baf09fb1df441b54e5e53e7ffb
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

<<<<<<< HEAD
=======
    item.name = row[0]
    item.save()
>>>>>>> a904ec6f838906e6c9675b4f00e8d27a9a1fc937
    des = Designer()
    des.name = row[0]
    des.save()
>>>>>>> cd04f8f83ca6b94d96e666034b672567432805db
=======
>>>>>>> 5fb667537c08794ab1c7eaef1b8d5148f49960a5
>>>>>>> 40821969a4f630baf09fb1df441b54e5e53e7ffb

        
