from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'welcome/index.html', {})
