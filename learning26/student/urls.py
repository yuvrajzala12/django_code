from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('demo/',views.demo),
    path('result/',views.result),
    path('phoneno/',views.phoneno),
    path('PF/',views.PF)
]