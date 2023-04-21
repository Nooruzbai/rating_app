from rest_framework import serializers
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from school_rating.models import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['comment', 'date_created']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise ValidationError("User has already liked the comment")


class CommentDislikeSerializer(serializers.ModelSerializer):
    pass



