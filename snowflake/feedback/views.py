from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from feedback.models import *

def home(request):
    return render_to_response('feedback/feedback.html')

def feedback_submit(request):
    form = Feedback.objects.create(subject=request.GET['subject'])
    form.save()
    form.message = request.GET['message']
    form.sender = request.GET['sender']
    form.save()
    return HttpResponse("Thanks! We value your feedback.")
