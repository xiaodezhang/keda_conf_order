from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'conf_order/index.html')

def myorder(request):
    return render(request,'conf_order/myorder.html')
