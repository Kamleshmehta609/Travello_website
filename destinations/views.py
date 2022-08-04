from django.shortcuts import render

# Create your views here.
def Mumbai(request):
    return render(request,'Mumbai.html')

def Hyderabad(request):
    return render(request,'Hyderabad.html')

def Pune(request):
    return render(request,'Pune.html')