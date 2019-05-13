from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('other/', views.other_page, name='other'),
   path('list/', views.SampleListView.as_view(), name='list'),
   path('create/', views.SampleCreateView.as_view(), name='create'),
]