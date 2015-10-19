from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

def summary(request):
    context = RequestContext(request)
    if request.method == 'POST':
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')

def home(request):
    return render_to_response('home.html', RequestContext(request, {}))
