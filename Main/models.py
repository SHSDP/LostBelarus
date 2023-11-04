from django.db import models
from ckeditor.fields import RichTextField

types_builds = [
    ('Замок','Замок'),
    ('Ратуша','Ратуша',),
    ('Православный храм','Православный храм',),
    ('Католический храм','Католический храм',),
    ('Синагога','Синагога',),
    ('Дворец/Усадьба','Дворец/Усадьба',),
    ('Разное','Разное',)
    ]

class Image (models.Model):
    path = models.TextField()
    name = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    sourc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class ArhetectureObject(models.Model):
    name = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    type_build =  models.CharField(max_length=50, choices=types_builds)
    overview = models.TextField()
    locality = models.CharField(max_length=50)
    sources = models.overview = models.TextField()
    
    
    def __str__(self):
        return self.name
    
    
    
    
class ArhetectureImage(Image):
    build = models.ForeignKey(ArhetectureObject, on_delete=models.CASCADE, related_name='arh_image')
    

    
    
    
class CityObject(models.Model):
    name = models.CharField(max_length=50)
    x = models.FloatField()
    y = models.FloatField() 
      
    def __str__(self):
        return self.name
    
    
class CityImage(Image):
    type_img =  models.CharField(max_length=50, choices=[('Изображение','Изображение'),('План/Карта','План/Карта')])
    locality = models.ForeignKey(CityObject, on_delete=models.CASCADE, related_name='city_image')
    
    
    
class ArtifactObject(models.Model):
    name = models.CharField(max_length=50)
    overview = models.TextField()
    sources = RichTextField()
    path_image = models.TextField()
    name_image = models.CharField(max_length=100)
    autor_image = models.CharField(max_length=50)
    sourc_image = models.CharField(max_length=100)
    chapter_image = models.TextField()
    
      
    def __str__(self):
        return self.name.replace('<br>',' ')