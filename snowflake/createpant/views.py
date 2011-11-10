from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from createpant.models import *
from django.views.decorators.csrf import csrf_exempt
from snowflake.functions import *
from snowflake.vars import *

def create(request):
	return render_to_response("base_create.html")

@csrf_exempt
def submit(request):
	pant = UserPant.objects.create(designer=str(request.POST['designer']))
	pant.save()
	pant.style = str(request.POST['style'])
	pant.label_waist = float(str(request.POST['label_waist']))
	pant.label_inseam = float(str(request.POST['label_inseam']))
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
