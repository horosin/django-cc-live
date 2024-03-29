from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
import json


from . import models


# Create your views here.
def index(request):
    return HttpResponse('Index page')


@permission_required('samples.view_sample')
def other_page(request):
    first_sample = models.Sample.objects.first()
    plot = {
        'x': json.dumps([1, 2, 3, 4, 5, 6]),
        'y': json.dumps([1, 2, 4, 8, 16, 1])
    }
    context = {
        'test': first_sample,
        'plot': plot
    }
    return render(request, 'samples/other.html', context)


class SampleListView(generic.ListView):
    model = models.Sample


class SampleCreateView(PermissionRequiredMixin, generic.CreateView):
    model = models.Sample
    fields = '__all__'
    success_url = reverse_lazy('list')
    permission_required = 'samples.create_sample'
