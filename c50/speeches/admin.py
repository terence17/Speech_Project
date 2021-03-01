from django.contrib import admin
from .models import Speaker
from .models import Speech

# Register your models here.
admin.site.register(Speaker)
admin.site.register(Speech)