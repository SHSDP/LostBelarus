from django.contrib import admin
from .models import *

class ChildInline(admin.TabularInline):
    model = ArhetectureImage
    extra = 1
    
@admin.register(ArhetectureObject)
class ModelArhetecture(admin.ModelAdmin):
    inlines = [ChildInline]
    fieldsets = (
        ('General information', {
            'fields': ('name', 'overview', 'sources','type_build'),
        }),
        ('Location', {
            'fields': ('x', 'y', 'locality',),
       }
    )
    )
    
    
    

class ChildInline2(admin.TabularInline):
    model = CityImage
    extra = 2
    
@admin.register(CityObject)
class ModelCityView(admin.ModelAdmin):
    inlines = [ChildInline2]


admin.site.register(ArtifactObject)