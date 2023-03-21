from django.urls import path
from .views  import home,registion

urlpatterns=[
    path('home/',home,name='home'),
    path('register/',registion,name='registion'),
    
]