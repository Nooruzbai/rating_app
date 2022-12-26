from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, UserAPIView, \
    UserProfileAPIView, UserAvatarAPIView

app_name = 'accounts'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='register' ),
    path('api/login/', UserLoginAPIView.as_view(), name="login-user"),
    path('api/logout/', UserLogoutAPIView.as_view(), name="logout-user"),
    path('api/detail/', UserAPIView.as_view(), name="user-info"),
    path('api/profile/', UserProfileAPIView.as_view(), name="user-profile"),
    path('api/profile/avatar/', UserAvatarAPIView.as_view(), name="user-avatar"),

]