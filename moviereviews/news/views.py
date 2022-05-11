from django.shortcuts import render

# Create your views here.
from . import models as newsModel


def news(request):
    template_name = "news/index.html"
    news_objects = newsModel.News.objects.all().order_by("-date")
    context = {
        "news_objects" : news_objects
    }
    return render(request, template_name,context)