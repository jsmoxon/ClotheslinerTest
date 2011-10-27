from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from clothes.models import *
from snowflake.vars import *

def compare_pants(reference_pant, reference_measurements, reference_margins_of_error, reference_flags):
	q = Pant.objects.all()
	for category, measurement in reference_measurements.items():
		if ("Unhemmed" in reference_flags) and (category == 'inseam'):
			q = q.filter(designer_inseam__exact = 0.0)
		else:
			measurement = float(str(measurement))
			moe = reference_margins_of_error[category]
			kwargs = {'%s__%s' % (category, 'range'): (measurement-moe, measurement+moe)}
			q = q.filter(**kwargs)
	q = q.exclude(id=reference_pant.id)
	return q 

def find_pants(designer, style, waist, inseam):
	flags = []
	kwargs = {}
	kwargs["designer__exact"]=designer
	kwargs["style__exact"]=style
	kwargs["designer_waist__exact"]=waist
	if inseam == "Unhemmed":
		kwargs["designer_inseam__exact"]=0.0
		flags.append("Unhemmed")
	else:
		kwargs["designer_inseam__exact"]=inseam
	try:
		return (Pant.objects.get(**kwargs), flags)	
	except Pant.DoesNotExist:
		return
	except Pant.MultipleObjectsReturned:
		a = Pant.objects.filter(**kwargs)
		return(a[0], flags)

def little_compare(num1, num2, key):
	if num1 == None:
		return "No data for reference pant"
	if num2 == None:
		return "No Data for this pant"
	usage = BIG_DICT[key]
	diff = float(num1 - num2)
	if diff == 0:
		return usage['zero']
	elif diff > 0:
		for k, v in iter(sorted(usage['positive'].iteritems())):
			if diff <= k: 
				return v 
	elif diff < 0:
		for k, v in iter(sorted(usage['negative'].iteritems())):
			if abs(diff) <= k:
				return v
	else:
		return "you messed up somewhere"

def narrow_pants(pants, filters):
	for filt in filters:
		fil = filt.split(', ')
		for pant in pants.keys():
			if pants[pant][fil[0]] != fil[1]:
				pants.pop(pant)
	return pants

def categorical_pant_list(ref, results):
	newList = {}
	for pant in results:
		newV = {}
		for k,v in pant.attrs():
			if k in BIG_DICT:
				newV[k] = little_compare(getattr(ref,k), v, k)
		newList[pant]=newV
	return newList
