from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from clothes.models import *
from snowflake.functions import *
from snowflake.vars import *

def landing(request):
	return render_to_response('landingPage.html')

def home(request):
	q = Pant.objects.all()
	r = {}
	for pant in q:
		if pant.designer in r and pant.style in r[pant.designer]:
			r[pant.designer][pant.style].append(pant)
		elif pant.designer in r:
			r[pant.designer][pant.style]=[pant]
		else:
			r[pant.designer]={pant.style:[pant]}
	return render_to_response('home.html', {'measurements':r}, context_instance=RequestContext(request))

def results(request):
	measurements = str.split(str(request.POST.get('measurements')))
	waist = measurements[0]
	inseam = measurements[2]
	designer = request.POST.get('designers')
	style = request.POST.get('styles')
	reference_pant, flags = find_pants(designer, style, waist, inseam)
	if not reference_pant:
		return redirect(home)
	else:
		compare_measurements = {"waist": reference_pant.waist, 
								"inseam": reference_pant.inseam,
								"cuff": reference_pant.cuff,
								"front_rise": reference_pant.front_rise}
		acceptable_pants = compare_pants(compare_measurements, MOE, flags)
		translated = categorical_pant_list(reference_pant, acceptable_pants)
		return render_to_response('results.html', {'pants':translated, 'reference':reference_pant}, context_instance=RequestContext(request))

def product_info(request):
	return HttpResponse("product info")
	
	
def about(request):
	return render_to_response('base_about.html', {},)
	
def compare(request):
	return render_to_response('base_compare.html', {},)
	
def logout(request):
	return render_to_response('base_outsuccess.html', {},)

def create(request):
	return render_to_response('base_create.html', {},)		
