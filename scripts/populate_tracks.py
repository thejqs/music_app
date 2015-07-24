import requests
import json
import simplejson as json

sys.path.append("..")

os environ.setdefault("DJANGO SETTINGS MODULE", "projects.settings")

from main.models import Tracks

response = request.get('http://freemusicarchive.org/api/get.albums.join?api_key=WML3781G7MGOWCRP')

response_dict = response.json()