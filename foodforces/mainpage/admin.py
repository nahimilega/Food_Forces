from django.contrib import admin

from .models import user,order

admin.site.register(user)
admin.site.register(order)