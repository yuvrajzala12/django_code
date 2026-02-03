from django.shortcuts import render

def home(request):
    return render(request,"student/home.html")

def demo(request):
    return render(request,"student/demo.html")

def result(request):
    return render(request,"student/result.html")

def phoneno(request):
    return render(request,"student/phoneno.html")

def PF(request):
    return render(request,"student/PF")
