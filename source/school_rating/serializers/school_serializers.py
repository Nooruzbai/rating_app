from rest_framework import serializers
from school_rating.models import School, SchoolRating



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'type', 'address', 'setting', 'webpage']

class SchoolRatingSerializer(serializers.ModelSerializer):
    rating = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = SchoolRating
        fields = ['rating', 'score', 'date_created']

class SchoolDetailSerializer(serializers.ModelSerializer):
    ratings = SchoolRatingSerializer(source='school_ratings', many=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'type', 'address', 'setting', 'webpage', 'ratings']