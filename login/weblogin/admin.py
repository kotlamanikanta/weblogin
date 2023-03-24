from django.contrib import admin
from.models import registion


class registerAdmin(admin.ModelAdmin):
    list_display=('username','email','password')

admin.site.register(registion)

# Register your models here.
