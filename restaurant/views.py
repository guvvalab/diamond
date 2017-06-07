from django.shortcuts import render
from django.http import HttpResponse

def detail(request):
    menu= {'Idly': 20, 'Vada': 25, 'Dosa': 28}
    menu1= {'Chicken Biryani': 200, 'Mutton Biryani': 290, 'Prawn Biryani': 300 }
    return render(request, "restaurant/detail.html",{'menu': menu, 'menu1': menu1})
