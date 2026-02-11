from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.user),
    path('talent_profile/',views.talent_profile),
    path('rating_review/',views.rating_review),
    path('message/',views.message),
    path('booking/',views.booking),
]
