from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
  model = Profile
  fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(required=True)
  class Meta:
    model = User
    fields = '__all__'

  def create(self, validated_data):
    user