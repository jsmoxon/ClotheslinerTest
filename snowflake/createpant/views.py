from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from createpant.models import *
from clothes.models import *
from django.views.decorators.csrf import csrf_exempt
from snowflake.functions import *
from snowflake.vars import *
# related to emailing us about a new pant upload

def create(request):
	return render_to_response("base_create.html")

@csrf_exempt
def submit(request):
	style_list = Style.objects.all()
	style_list_two = []
	designer_objects = Designer.objects.all()
	designer_list = []
	for obj in style_list:
		style_list_two += [obj.name]
	for des in designer_objects:
		designer_list += [des.name]
	designer = str(request.POST['designer'])
	style = str(request.POST['style'])
	print designer_list
	if designer not in designer_list:
		ndesigner = Designer()
		ndesigner.name = designer
		ndesigner.save()
	else:
		ndesigner = str(request.POST['designer'])
	if style not in style_list_two:
		nstyle = Style()
		nstyle.name = style
		nstyle.save()
	else:
		nstyle = str(request.POST['style'])
	pant = Pant()
	pant.designer = Designer.objects.get(name = ndesigner)
	pant.style = Style.objects.get(name = nstyle)
	pant.designer_waist = float(str(request.POST['label_waist']))
	pant.designer_inseam = float(str(request.POST['label_inseam']))
	pant.waist = float(str(request.POST['waist']))
	pant.inseam = float(str(request.POST['inseam']))
	pant.front_rise = float(str(request.POST['front_rise']))
	pant.back_rise = float(str(request.POST['back_rise']))
	pant.thigh = float(str(request.POST['thigh']))
	pant.hips = float(str(request.POST['hips']))
	pant.knee = float(str(request.POST['knee']))
	pant.cuff = float(str(request.POST['cuff']))
	pant.outseam = float(str(request.POST['outseam']))
	pant.save()
	request.session["reference_pant"] = pant
	request.session["flags"] = []
	request.session["result_set"] = None
	request.session["filters"] = []
       	return HttpResponseRedirect(reverse('clothes.views.results'))

