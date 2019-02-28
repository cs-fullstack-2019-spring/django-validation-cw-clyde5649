from django.shortcuts import render
from .models import ModelForm
from django.http import HttpResponse
from .forms import Userform
# Create your views here.


def index(request):


    if(request.method == 'Post'):
        form = Userform(request.POST)


    if(form.is_valid()):


        return render(request, "CarsApp/index.html")