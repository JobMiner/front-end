from django.contrib import admin

# Register your models here.
from fetch.models import Creator

class CreatorAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name']
    list_display = ('first_name', 'last_name')

admin.site.register(Creator, CreatorAdmin)