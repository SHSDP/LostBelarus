from django.shortcuts import render 
from .models import *

def index(request):
    return render(request,'index.html')



def arhetecture(request):
    objects =  ArhetectureObject.objects.all()
    return render(request,'arhetecture.html',context = {'objs': objects,})


def arh_object(request, id):
    object =  ArhetectureObject.objects.get(pk=id)
    return render(request,'arh-object.html', context = {'obj': object,})




def cities_views(request):
    objects =  CityObject.objects.all() 
    return render(request,'cities-views.html',context = {'objs': objects,})

def city_views(request, id):
    object =  CityObject.objects.get(pk=id).city_image.filter(type_img= 'Изображение' )  
    object2 =  CityObject.objects.get(pk=id).city_image.filter(type_img= 'План/Карта')
    return render(request,'city-view.html',context = {'obj': object, 'obj2': object2,})





def artifacts_views(request):
    objects =  ArtifactObject.objects.all()  
    return render(request,'artifacts.html',context = {'objs': objects,})

def artifact_view(request, id):
    object =  ArtifactObject.objects.get(pk=id)
    return render(request,'arf-object.html', context = {'obj': object})





