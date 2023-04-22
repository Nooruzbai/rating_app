from rest_framework import serializers
from school_rating.models import School, SchoolRating
from school_rating.serializers.comment_serializers import SchoolCommentSerializer


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'type', 'address', 'setting', 'webpage']


class SchoolRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolRating
        fields = ['rating', 'score', 'date_created']


class SchoolDetailSerializer(serializers.ModelSerializer):
    ratings = SchoolRatingSerializer(many=True)
    comments = SchoolCommentSerializer(many=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'description', 'type', 'address', 'setting', 'webpage', 'ratings',  'comments']