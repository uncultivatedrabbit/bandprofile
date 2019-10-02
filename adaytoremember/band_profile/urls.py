from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adtr/', views.adtr, name='adtr'),
    path('albums', views.albums, name="albums"),
    path('adtr/<str:name>'.lower(), views.bio, name="bio"),
    path('albums/<str:slug>'.lower(), views.album, name="album")
]
