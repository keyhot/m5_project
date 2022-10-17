from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer, MovieReviewListSerializer
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def directors_view(request):
    movies = Director.objects.all()
    data = DirectorListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    data = MovieListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_review_view(request):
    movies = Movie.objects.all()
    data = MovieReviewListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    data = DirectorListSerializer(director)
    return Response(data=data.data)


@api_view(['GET'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    data = MovieListSerializer(movie)
    return Response(data=data.data)


@api_view(['GET'])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    data = ReviewListSerializer(review)
    return Response(data=data.data)
