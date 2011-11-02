from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from clothes.models import *
from snowflake.functions import *
from snowflake.vars import *
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

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
	reference_pant = request.session["reference_pant"]
	flags = request.session["flags"]
	result_set = request.session["result_set"]
	filters = str(request.POST.get("filter", ""))
	token = get_token(request)
	
	if filters != "":
		filters = filters.split(')(')
		filters[0] = filters[0][1:]
		filters[-1] = filters[-1][:-1]
	
	if result_set == None:
		compare_measurements = {"waist": reference_pant.waist, 
								"inseam": reference_pant.inseam,
								"cuff": reference_pant.cuff,
								"front_rise": reference_pant.front_rise}
		acceptable_pants = compare_pants(reference_pant, compare_measurements, MOE, flags)
		translated = categorical_pant_list(reference_pant, acceptable_pants)
		request.session["result_set"] = translated.copy()
	else:
		translated = narrow_pants(result_set.copy(), filters)
	
	return render_to_response('results.html', {'pants':translated, 'reference':reference_pant, 'filters':filters, 'token':token}, context_instance=RequestContext(request))

def find_reference(request):
	measurements = str.split(str(request.POST.get('measurements')))
	waist = measurements[0]
	inseam = measurements[2]
	designer = request.POST.get('designers')
	style = request.POST.get('styles')
	reference_pant, flags = find_pants(designer, style, waist, inseam)
	if not reference_pant:
		return redirect(home)
	else:
		request.session["reference_pant"] = reference_pant
		request.session["flags"] = flags
		request.session["result_set"] = None
		request.session["filters"] = []
		return HttpResponseRedirect(reverse('clothes.views.results'))

def product_info(request, comp):
	reference_pant = request.session["reference_pant"]
	compared_pant = Pant.objects.get(id__exact = comp)
	return render_to_response('product_info.html', {'compared':compared_pant, 'reference':reference_pant}, context_instance=RequestContext(request))

def super_compare(request):
	shopping_cart = request.session["shopping_cart"]
	reference_pant = request.session["shopping_cart"]
	return render_to_response('super_compare.html', {'reference':reference_pant, 'shopping':shopping_cart}, context_instance=RequestContext(request))

def about(request):
	return render_to_response('base_about.html', {},)

def compare(request):
	return render_to_response('base_compare.html', {},)

def logout(request):
	return render_to_response('base_outsuccess.html', {},)

def create(request):
	return render_to_response('base_create.html', {},)	
