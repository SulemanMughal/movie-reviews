from django.contrib import admin

# Register your models here.

from . import models as newsModel

admin.site.register(newsModel.News)