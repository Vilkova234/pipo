from django.shortcuts import render
from .models import *
from django.views.generic import ListView
# Create your views here.

# views.py
def catalog(request):
    movies = Movie.objects.all()
    return render(request, 'movie/catalog.html',{
        'movies' : movies
    })  

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == "POST":
        text_review = request.POST.get("review_text")
        MovieReview.objects.create(
            author = request.user,
            movie = movie,
            text = text_review,
            
        )

    return render(request, 'movie/movie_detail.html',{
        'movie' : movie
    })  


