from ArtistZoneAdministration.models import Personas
from django.contrib import admin
from .models import Task, ImagenesIndex
# Register your models here.
admin.site.register(Personas)
admin.site.register(Task)
admin.site.register(ImagenesIndex)