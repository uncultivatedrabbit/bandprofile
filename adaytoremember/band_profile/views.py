from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404
from .models import BandMember, Album

# Create your views here.
def index(request):
  context = {
    "band_member": BandMember.objects.all(),
    "album": Album.objects.all()
  }
  return render(request, "band_profile/index.html", context)