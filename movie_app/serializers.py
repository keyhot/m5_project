from rest_framework import serializers
from .models import Director, Movie, Review
from django.db.models import Avg


class DirectorListSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()

    def get_movies_count(self, obj_director):
        return Movie.objects.filter(director=obj_director).count()


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director'.split()


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()


class MovieReviewListSerializer(serializers.ModelSerializer):
    stars = serializers.SerializerMethodField()
    reviews = ReviewListSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title description duration director reviews stars'.split()

    def get_stars(self, movie_obj):
        return Review.objects.filter(movie=movie_obj).aggregate(Avg('stars'))['stars__avg']
