from django.contrib import admin
from .models import Gallery, Photo

# This tells Django to show these tables in the Admin dashboard
admin.site.register(Gallery)
admin.site.register(Photo)