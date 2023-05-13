from django.shortcuts import render
# Create your views here.

def baby(request):
    return render(request,'gallary/Dinner.html')

def country(request):
    return render(request,'gallary/Party.html')

def product(request):
    return render(request,'gallary/Wedding.html')
