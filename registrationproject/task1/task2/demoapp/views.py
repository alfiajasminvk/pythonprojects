from django.shortcuts import render
from .models import Place,Team
# Create your views here.
def index(request):
    obj1=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html',{"obj1":obj1,"obj2":obj2})