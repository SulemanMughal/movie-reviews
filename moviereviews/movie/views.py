from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404 , redirect

# Create your views here.

# ? import local modals
from . import models as movieModels

# ? import local forms
from .forms import ReviewForm

def home(request):
    template_name = "movie/home.html"
    movies = movieModels.Movie.objects.all()
    context = {
        "movies" : movies
    }
    return render(request, template_name, context)


def search(request):
    template_name = "movie/home.html"

    # ? Get search parameter 
    q = request.GET.get("q", None)
    if q:
        movies = movieModels.Movie.objects.filter(title__icontains = q)
    else:
        movies = movieModels.Movie.objects.all()
    context = {
        "movies" : movies,
        "query" : q,
    }
    return render(request, template_name, context)


def details(request, movieID):
    template_name = "movie/details.html"
    movie = movieModels.Movie.objects.get(id=movieID)
    reviews = movieModels.Review.objects.filter(movie = movie)
    context = {
        "movie" : movie,
        'reviews': reviews
    }
    return render(request, template_name, context)

@login_required
def createReview(request, movie_id):
    template_name = "movie/createreview.html"
    movie = get_object_or_404(movieModels.Movie,pk=movie_id)
    if request.method == 'GET':
        context= {'form':ReviewForm(), 'movie': movie}
        return render(request, template_name, context)
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('details', newReview.movie.id)
        except ValueError:
            context={'form':ReviewForm(),'error':'bad data passed in'}
            return render(request,template_name,context)

@login_required
def updateReview(request, review_id):
    review = get_object_or_404(movieModels.Review,pk=review_id,user=request.user)
    if request.method =='GET':
        form = ReviewForm(instance=review)
        return render(request, 'movie/updatereview.html',
        {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('details', review.movie.id)
        except ValueError:
            return render(request, 'movie/updatereview.html',
            {'review': review,'form':form,'error':'Bad data in form'})

@login_required
def deleteReview(request, review_id):
    review = get_object_or_404(movieModels.Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('details', review.movie.id)