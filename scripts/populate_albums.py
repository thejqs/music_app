#!/usr/bin/env python
import sys, os
import requests
import json
from StringIO import StringIO

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Albums, Artists
from django.conf import settings

import django
django.setup

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


payload = {'api_key': settings.FMA_API_KEY, 'limit': 100}

response = requests.get('http://freemusicarchive.org/api/get/albums.json', params=payload)

response_dict = response.json()

for data in response_dict['dataset']:
    album, created = Albums.objects.get_or_create(album_id=data.get('album_id'))
    album.album_title = data.get('album_title')
    print album.album_title
    album.album_info = data.get('album_info')

    artist_name = data.get('artist_name')
    print artist_name
    payload = {'artist_name': artist_name}
    artist_response = requests.get('http://freemusicarchive.org/api/get/artists.json?api_key=WML3781G7MGOWCRP', params=payload)
    artist_dict = artist_response.json()
    artist_id = artist_dict['dataset'][0]['artist_id']

    artist, created = Artists.objects.get_or_create(artist_id=artist_id, artist_name=data.get('artist_name'))
    album.artist = artist
    temp_image = NamedTemporaryFile(delete=True)

    album_image = requests.get(data.get('album_image_file'))

    temp_image.write(album_image.content)

    album.album_image = File(temp_image)

    album.save()


# print response_dict['dataset'][0].keys()





# album_id = models.IntegerField(primary_key=True)
# artist = models.ForeignKey('main.Artists', null=True)
# album_title = models.CharField(max_length=255, null=True)
# album_date = models.DateTimeField(default="")
# album_image = models.ImageField(upload_to="album_imag