from rest_framework import serializers

from school_rating.models import School, Rating, SchoolRating


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'type', 'address', 'setting', 'webpage']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['name', 'date_crated']


class SchoolRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolRating
        fields = ['school', 'rating', 'score', 'date_created']

