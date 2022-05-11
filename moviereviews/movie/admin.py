from django.contrib import admin

# Register your models here.
from . import models as movieModels

admin.site.register(movieModels.Movie)
admin.site.register(movieModels.Review)
