import jwt
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Profile, CustomUser
from accounts.serializers import UserRegistrationSerializer, UserLoginSerializer, CustomUserSerializer, \
    ProfileSerializer, ProfileAvatarSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema

from accounts.utils import Util

User = get_user_model()




class UserRegistrationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        operation_summary="User Registration",
        operation_description="Returns data consisting Tokens and additional information about the user"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user)
        current_site = get_current_site(request).domain
        relative_link = reverse('accounts:verify_email')
        absolute_url = 'http://'+current_site+relative_link+"?token="+str(token.access_token)
        print(absolute_url)
        email_body = 'Hi ' + user.username+' Use link below to verify your email\n'+absolute_url
        data = {"email_body": email_body, "to_email": user.email, "email_subject":"Verify your email",
                "tokens": {"refresh_token": str(token), "refresh": str(token.access_token)}}
        # Util.send_email(data)
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(
        operation_summary="User Login",
        operation_description="Returns a token"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)

class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    @swagger_auto_schema(
        operation_summary="User Logout",
    )
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user information
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user

class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user profile
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile

class UserAvatarAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user avatar
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileAvatarSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile

class VerifyEmail(GenericAPIView):
    serializer_class = CustomUserSerializer

    @swagger_auto_schema(
        operation_summary="User Verification by email"
    )
    def get(self, request, args, **kwargs):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
               user.is_verified = True
               user.save()
            return  Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
