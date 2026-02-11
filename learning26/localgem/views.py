from django.shortcuts import render

# Create your views here.

def user(request):
    return render(request,"localgem/user.html")

def talent_profile(request):
    return render(request,"localgem/talent_profile.html")

def rating_review(request):
    return render(request,"localgem/rating_review.html")

def message(request):
    return render(request,"localgem/message.html")

def booking(request):
    return render(request,"localgem/booking.html")