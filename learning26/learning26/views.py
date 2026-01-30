from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"AboutUs.html")

def contactUs(request):
    return render(request,"contactUs.html")

def home(request):
    return render(request,"home.html")


def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient} 
    return render(request,"recipe.html",data)

def movies(request):
    return render(request,"movies.html")

def team(request):
    playerlist = ["virat", "dhoni"]
    data = {"name": "virat","trophy":4,"playerlist":playerlist}
    return render(request,"team.html",data)


