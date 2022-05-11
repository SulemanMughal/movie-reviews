from django.conf.urls import url
from django.urls import path

from . import views as movieViews

urlpatterns = [
    url(r'^$', movieViews.home, name="home"),
    url(r'^search/$', movieViews.search, name="search"),
    path("movie/details/<int:movieID>",movieViews.details,name="details"),
    path("movie/<int:movie_id>/create/review", movieViews.createReview, name="create_review"),
    path("update/review/<int:review_id>", movieViews.updateReview, name="update_review"),
    path('delete/review/<int:review_id>', movieViews.deleteReview, name='delete_review'),

]