from django.shortcuts import render

# Create your views here.
def view(request):
    return rennder(request, 'app_landing/index.html')