from django.contrib import admin

#local imports
from .models import Link
from .models import Profile

# Register your models here.

admin.site.register(Link)
admin.site.register(Profile)