from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'appname/index.html')

def about(request):
    return render(request, 'appname/about.html')
