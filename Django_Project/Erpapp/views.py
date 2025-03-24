from django.shortcuts import render

# Create your views here.
# in this file we will make functions views.py file is main file in our project main business logic 
#in this each function returns html compulsory if and else then if also returns html and else also returns html 
#
def index(request):
    return render(request,"index.html")
