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

def bio(request, name):
  
  first_name = name.split('-', 1)[0].capitalize()

  context = {
    "band_member": BandMember.objects.get(first=first_name),
    "albums": Album.objects.all(),
    "songs": Song.objects.all()
  }

  return render(request, "band_profile/bio.html", context)

# def jeremymckinnon(request):
#   return render(request, "band_profile/jeremymckinnon.html")

def neilwestfall(request):
  return render(request, "band_profile/neilwestfall.html")