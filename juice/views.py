from django.http import HttpResponse
from django.shortcuts import render
from . import models
import json

def index(request):
    objects = models.JuiceMenu.objects.all()
    menu = {'name':'apple', 'price': 30, 'mango': 20, 'grape':10}
    return render(request, "juice/detail.html", {'data' : objects, 'data2' : menu})
    #return HttpResponse(json.dumps(menu))

def applejuice(request):
    menu = {'apple': 30, 'mango': 20, 'grape':10}
    return render(request, "juice/detail.html", {'menu': menu})

def update_juice(request, pk):
	obj = models.JuiceMenu.objects.get(s_no= pk)
	
	return render(request, "juice/update_juice.html",{'data': obj})
	#return HttpResponse('juice/update_juice.html') 

	#return HttpResponse('you have selected '+ str(obj))
