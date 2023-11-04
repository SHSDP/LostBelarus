from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('arhetecture', views.arhetecture, name='arhetecture'),
    path('arhetecture/<int:id>', views.arh_object, name='arh-object'),
    path('cities-views', views.cities_views, name='cities-views'),
    path('city-view/<int:id>', views.city_views, name='city-view'),
    path('artifacts', views.artifacts_views, name='artifacts_views'),
    path('artifacts/<int:id>', views.artifact_view, name='artifact-view'),
    
]
