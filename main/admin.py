from django.contrib import admin
from main.models import Genres, Artists, Albums, Tracks
from main.models import CustomUserManager, CustomUser

admin.site.register(Genres)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(Tracks)
# admin.site.register(CustomUserManager)
# admin.site.register(CustomUser)