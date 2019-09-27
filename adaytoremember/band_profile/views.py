from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404
from .models import BandMember, Album, Song

# Create your views here.
def index(request):
  context = {
    "band_members": BandMember.objects.all(),
    "albums": Album.objects.all(),
    "songs": Song.objects.all()
  }
  return render(request, "band_profile/index.html", context)

def adtr(request):
  context = {
    "band_members": BandMember.objects.all(),
    "albums": Album.objects.all(),
    "songs": Song.objects.all()
  }
  return render(request, 'band_profile/grid-view.html', context)