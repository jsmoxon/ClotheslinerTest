from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from clothes.models import *
from snowflake.functions import *
from snowflake.vars import *
from snowflake.fitdict import *
from snowflake.deepdict import *
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

def landing(request):
	return render_to_response('landingPage.html')

def home(request):
	q = Pant.objects.all()
	r = {}
	for pant in q:
		des = str(pant.designer.name)
		sty = str(pant.style.name)
		desID = int(pant.designer.id)
		styID = int(pant.style.id)
		if des in r and sty in r[des]:
			r[des][sty].append([pant.designer_waist, pant.designer_inseam, desID, styID])
		elif des in r:
			r[des][sty]=[[pant.designer_waist, pant.designer_inseam, desID, styID]]
		else:
			r[des]={sty:[[pant.designer_waist, pant.designer_inseam, desID, styID]]}
	measure = simplejson.dumps(r)
	return render_to_response('home.html', {'measurements':measure}, context_instance=RequestContext(request))

def results(request):
	reference_pant = request.session["reference_pant"]
	flags = request.session["flags"]
	result_set = request.session["result_set"]
	filters = str(request.POST.get("filter", ""))
	fittingRoom = str(request.POST.get("fitRoom", ""))
	token = get_token(request)
	
	if fittingRoom != "":
		fitting_item = Pant.objects.get(pk=fittingRoom)
		request.session["fitting_room"].append(fitting_item) if (fitting_item not in request.session["fitting_room"]) else None
	
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
	
	return render_to_response('results.html', { 'pants':translated, 
												'reference':reference_pant, 
												'filters':filters, 
												'token':token }, context_instance=RequestContext(request))

def find_reference(request):
	measurements = str.split(str(request.POST.get('measurements')))
	waist = measurements[0]
	inseam = measurements[1]
	designer = measurements[2]
	style = measurements[3]
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

def super_compare(request, comp=None):
	sauce = simplejson.dumps(FIT_DICT)
	secret_sauce = simplejson.dumps(DEEP_DICT)
	not_secret_sauce = simplejson.dumps(SHALLOW_DICT)
	more_secret_sauce = simplejson.dumps(RIGHT_DICT)
	other_secret_sauce = simplejson.dumps(OTHER_DICT)
	token = get_token(request)
	fitRoom = []
	if str(request.POST.get("fitRoom", "")) != "":
		fittingRoom = str(request.POST.get("fitRoom", ""))
		fitRoom = fittingRoom.split(',')
	elif not comp:
		return HttpResponse(EXPLANATION)
	
	if not comp:
		comp = fitRoom[0]
	if comp not in fitRoom:
		fitRoom.append(int(comp))
	fitRoom = Pant.objects.filter(pk__in=fitRoom)
	compPant = Pant.objects.get(pk=comp)
	
	reference_pant = request.session["reference_pant"]
	return render_to_response('super_compare.html', {'reference':reference_pant, 
													 'fitRoom':fitRoom, 
													 'compared':compPant,
													 'sauce':sauce,
													 'specialSauce':secret_sauce,
													 'lessSpecialSauce':not_secret_sauce,
													 'moreSpecialSauce':more_secret_sauce,
													 'otherSpecialSauce':other_secret_sauce,
													 'token':token }, context_instance=RequestContext(request))

def about(request):
	return render_to_response('base_about.html', {},)

def compare(request):
	return render_to_response('base_compare.html', {},)

def logout(request):
	return render_to_response('base_outsuccess.html', {},)

def create(request):
	return render_to_response('base_create.html', {},)	

def drawnpantimage(request):
	return render_to_response('drawnpant.html', {},)

def liemphoto(request):
	return render_to_response('liemphoto.html', {},)

def test(request):
	return render_to_response('test.html', {},)
