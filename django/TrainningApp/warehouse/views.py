from django.shortcuts import render

from django.http import HttpResponse



# Create your views here.


def registerr(request):
    return render(request, 'template_register_warehouse.html', {})



