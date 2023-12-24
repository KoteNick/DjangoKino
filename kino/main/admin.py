from django.contrib import admin
from .models import Film
from .models import Hall

# Register your models here.
admin.site.register(Film)
admin.site.register(Hall)