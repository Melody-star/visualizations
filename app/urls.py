from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('api/student',views.personnum,name='personnum'),
    path('api/classroom',views.classroom,name='classroom'),
    path('api/news',views.news,name='classroom'),
    path('api/iotequipment',views.iotequipment,name='classroom'),
    path('api/controlsystem',views.controlsystem,name='classroom'),
    path('api/news',views.news,name='classroom'),
]