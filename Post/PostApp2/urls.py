

from django.urls import path,include
from .views import *
urlpatterns = [
    path('index2',index2 ,name = 'index2'),

]
