from django.contrib import admin

# Register your models here.
from .models import about,slider,client

admin.site.register(about)
admin.site.register(slider)
admin.site.register(client)