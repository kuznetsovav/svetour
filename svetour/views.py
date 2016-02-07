from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'svetour/home.html', {})

def andorra(request):
    return render(request, 'svetour/andorra.html', {})

def shusskiapthl(request):
    return render(request, 'svetour/shusskiapthl.html', {})