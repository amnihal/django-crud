from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.post_mark,name='post_mark'),
    path("update_mark/<str:id>",views.update_mark,name='update_mark'),
    path("remove_mark/<str:id>",views.remove_mark,name='remove_mark'),
    
    
    
    
]
