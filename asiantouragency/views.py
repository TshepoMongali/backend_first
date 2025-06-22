from django.shortcuts import render
from django.http import HttpResponse
from .models import Tour
# Create your views here.
def index(request):
    tours=Tour.objects.all()
    context = {'tour':tours}
    return render(request, 'tours/home.html',context)
