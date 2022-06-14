"""
This is Default Django Admin Config!
"""
from django.contrib import admin

from barcode_server.models import User, Result

# Register your models here.


admin.site.register(User)
admin.site.register(Result)
