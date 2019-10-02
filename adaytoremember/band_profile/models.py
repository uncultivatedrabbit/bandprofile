from django.db import models

# Create your models here.

class BandMember(models.Model):

  INSTRUMENTS = (
  ("LV", "Lead Vocals"),
  ("RG", "Rhythm Guitar"),
  ("BG", "Bass Guitar"),
  ("D", "Drums"),
  ("LG", "Lead Guitar")
  )

  first = models.CharField(max_length=64)
  last = models.CharField(max_length=64)
  instrument = models.CharField(max_length=64, choices=INSTRUMENTS)
  years_in_band = models.CharField(max_length=64)
  hometown = models.CharField(max_length=64)

  def __str__(self):
      return f"{self.first} {self.last}: {self.instrument}, ({self.years_in_band})"

class Album(models.Model):
  name = models.CharField(max_length=64)
  year = models.IntegerField()
  label = models.CharField(max_length=64)
  slug = models.SlugField(max_length=50, null=True, blank=True)
    
  def __str__(self):
      return f"{self.name} ({self.year})"


class Song(models.Model):
  name = models.CharField(max_length=64)
  time = models.CharField(max_length=10)
  trackNumber = models.IntegerField(blank=True, null=True)
  onAlbum = models.ForeignKey(Album, blank=True, null=True, on_delete=models.CASCADE, related_name="track")

  def __str__(self):
    if self.onAlbum:
      return f"{self.trackNumber}. {self.name} [{self.onAlbum}]"
    else:
      return f"{self.trackNumber}. {self.name}"



