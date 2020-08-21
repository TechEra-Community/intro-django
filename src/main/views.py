from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    l=[]
    for i in range(1,10):
        l.append(i)
    
    context={
        'youname':'something new',
        'list':l
    }
    return render(request,'index.html',context)