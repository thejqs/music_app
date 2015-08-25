#!/usr/bin/env python
import sys, os
import requests
import json
from StringIO import StringIO

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Artists
from django.conf import settings

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

payload = {'api_key': settings.FMA_API_KEY, 'limit': 500}

response = requests.get('http://freemusicarchive.org/api/get/artists.json', params=payload)

response_dict = response.json()

# print response_dict['dataset'][0].keys()

for data in response_dict['dataset']:
    artist, created = Artists.objects.get_or_create(artist_id=data.get('artist_id'))

    artist.artist_url = data.get('artist_url')
    artist.artist_name = data.get('artist_name')
    artist.artist_bio = data.get('artist_bio')
    artist.artist_slug = data.get('artist_slug')

    artist_image_request = requests.get(data.get('artist_image_file'))

    temp_image = NamedTemporaryFile(delete=True)
    temp_image.write(artist_image_request.content)

    artist.artist_image = File(temp_image)

    # print artist.artist_name
    artist.save()

Artists.objects.filter(artist_name=None).delete()
