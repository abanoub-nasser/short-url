from django.contrib import admin

from models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('id','Lurl','Surl', 'Views', 'Date')
    search_fields = ('id','Lurl','Surl','Views', 'Date')

admin.site.register(Url, UrlAdmin)
