from rest_framework import serializers
from school_rating.models import Rating, SchoolRating
from school_rating.serializers.school_serializers import SchoolRatingSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','name', 'date_created']


class RatingSchoolSerializer(serializers.ModelSerializer):
    school = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = SchoolRating
        fields = ['school', 'score', 'date_created']


class RatingDetailSerializer(serializers.ModelSerializer):
    schools = RatingSchoolSerializer(many=True, read_only=True)

    class Meta:
        model = Rating
        fields = ['name', 'date_created', 'schools']