from django.urls import path
from . import views

urlpatterns = [
    path('firstapp',views.home,name='home'),
    path('firstapp/test',views.get,name='get')

]
