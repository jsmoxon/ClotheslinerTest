from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from register.models import *

def register(request):
    form = registrant.objects.create(email=request.GET['email'])
    form.save()
    form.name = request.GET['name']
    form.save()
    return HttpResponse("Thanks! We'll be in touch.")

