from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from .models import CustomUser, Profile

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    
    """
    # bio = serializers.CharField(source='profile.bio')
    class Meta:
        model = User
        fields = ("id", "username", "email",'password','first_name', 'last_name',)


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """
    confirm_password = serializers.CharField(max_length=100, allow_blank=False, allow_null=False, write_only=True)
    first_name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False, error_messages={"requierd": "User must have a first name"})
    last_name = serializers.CharField(max_length=100, allow_blank=False, allow_null=False, error_messages={"requierd":"User must have a last name"})
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True},
                        }

    def validate(self, attrs):
        data = super(UserRegistrationSerializer, self).validate(attrs)
        password = data.get('password')
        confirm_password = data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Password mismatch')
        return data


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class ProfileSerializer(CustomUserSerializer):
    """
    Serializer class to serialize the user Profile model
    """

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAvatarSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize the avatar
    """

    class Meta:
        model = Profile
        fields = ("profile_picture",)