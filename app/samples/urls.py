from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('other/', views.other_page, name='other'),
]