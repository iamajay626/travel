from django.shortcuts import render
from django.http import HttpResponse
def demo(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

# Create your views here.
