from django.contrib import admin
from main1.models import Film, Director, Comments
# Register your models here.

admin.site.register(Director)
admin.site.register(Film)
admin.site.register(Comments)
