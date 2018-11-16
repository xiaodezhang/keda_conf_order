from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'conf_order/index.html')

def myorder(request):
    time_splits_array = [['8:00-9:00','9:00-10:00','10:00-11:30'],
            ['13:00-14:00','14:00-15:00','15:00-16:00'],
            ['16:00:17:30','18:00-19:00','19:00-20:00']]
    return render(request,'conf_order/myorder.html',{'time_splits_array':time_splits_array})
