from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic

from . import models


# Create your views here.
def index(request):
    return HttpResponse('Index page')


def other_page(request):
    first_sample = models.Sample.objects.first()
    context = {
        'test': first_sample
    }
    return render(request, 'samples/other.html', context)


class SampleListView(generic.ListView):
    model = models.Sample

class SampleCreateView(generic.CreateView):
   model = models.Sample
   fields = '__all__'
   success_url = reverse_lazy('list')
