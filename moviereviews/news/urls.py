from django.conf.urls import url

from . import views as newsViews

urlpatterns = [
    url(r'^$', newsViews.news, name="news"),
]