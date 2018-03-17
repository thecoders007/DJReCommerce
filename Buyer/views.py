from django.shortcuts import render

# Create your views here.


def Main(request):
    return render(request, 'Main.html')
