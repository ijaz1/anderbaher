from django.shortcuts import render

# Create your views here.

def fnClientHome(request):
    return render (request,'client_home.html')