from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'info/base.html')
    return render(request, 'info/index.html')  
