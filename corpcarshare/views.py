from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse

from .forms import eachpostform, eachcompanyform
from .models import eachpost, eachcompany

from django.views.generic import TemplateView
from django.views.generic.list import ListView, BaseListView

from django.views.generic import CreateView
from django.views.generic.edit import BaseCreateView
from django.views.generic.base import TemplateResponseMixin

from django.http import HttpResponse
from django.core.context_processors import csrf

import json
import urllib

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage




# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def home(request):
	if request.method == 'POST':
		form = eachpostform(request.POST)
		if form.is_valid():
			save_it = form.save(commit = False)
			save_it.save()
			Compname = request.POST.get('workname', None)
			Compaddr = request.POST.get('workaddr', None)
			Compzip = request.POST.get('workzip', None)
			comp_obj = eachcompany(compname = Compname, compzip = Compzip, compaddr = Compaddr)
			comp_obj.save()
			#send_mail('Your carpool candidates', 'Here is the message.', 'from@example.com', ['sywad87@gmail.com'], fail_silently=True) 
			#msg = EmailMessage('Request Callback','Here is the message.', to=['yiwei.song@sandisk.com'])
			#msg.send()
			results = eachpost.objects.all().order_by("-date")[:10]
			return render_to_response("corpcarshare.html", {'form': eachpostform(request.POST), 'object_list':results}, context_instance = RequestContext(request))

	else:
		form = eachpostform()
	content = match('95035', '94587')
	message = draftEmail(content)
	send_mail('Your carpool candidates', message, 'sywad87@gmail.com', ['sywad87@gmail.com'], fail_silently=True) 
	args = {}
	args.update(csrf(request))
	args['form'] = form 
	args['object_list'] = eachpost.objects.all().order_by("-date")[:10]
	companies = eachcompany.objects.all()
	name = []
	address = []
	for c in companies:
		#res.append(c.__unicode__())
		name.append(c.compname)
		address.append(c.compaddr)
	args['name'] = json.dumps(name)
	args['address'] = json.dumps(address)
	return render_to_response("corpcarshare.html", args, context_instance = RequestContext(request))




def nameauto(request):
    term = request.GET.get('term') #jquery-ui.autocomplete parameter
    names = eachcompany.objects.all() #lookup for a city
    res = []
    for c in names:
         #make dict with the metadatas that jquery-ui.autocomple needs (the documentation is your friend)
         #dict = {'id':c.id, 'label':c.__unicode__(), 'value':c.__unicode__()}
         #dict = {'label':c.__unicode__()}
         dict = c.__unicode__()
         res.append(dict)
    return HttpResponse(json.dumps(res), mimetype='application/json')


def distance(origin, destination):
	GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'
	url = GEOCODE_BASE_URL + '?' + 'origins='+origin + '&' + 'destinations=' + destination
	result = json.load(urllib.urlopen(url))
	status = result['rows'][0]['elements'][0]['status']
	if (status == 'OK'):
		return result['rows'][0]['elements'][0]['duration']['value']
	else:
		return 10000


def match(home, work):
	value = {}
	candidates = eachpost.objects.all()
	for candidate in candidates:
		#print candidate.workzip
		value[candidate] = distance(home, candidate.homezip) + distance(work, candidate.workzip)
		print value[candidate]
	target = min(value, key=value.get)
	result = [target.email, target.homezip, target.workzip]
	return result

def draftEmail(content):
	message = 'Here is your mate: ' + 'email: '+ content[0] + ' home address: ' + content[1] + ' work address: ' + content[2]
	return message

