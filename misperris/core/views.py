from django.shortcuts import render
from .models import huerfano


# Create your views here.
def index(request):
    dog = huerfano.objects.all()
    return render(request,"core/index.html",{'dog' : dog})
