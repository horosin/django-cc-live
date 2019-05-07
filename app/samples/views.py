from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Index page')


def other_page(request):
   context = {
       'test': 'passing a value to the template'
   }
   return render(request, 'samples/other.html', context)

