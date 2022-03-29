from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html')
def bye(request):
    return render(request,'bye.html')