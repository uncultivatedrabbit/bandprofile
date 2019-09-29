from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adtr', views.adtr, name='adtr'),
    path('<str:name>'.lower(), views.bio, name="bio"),
    path('neil-westfall', views.neilwestfall, name="neil-westfall")
]
