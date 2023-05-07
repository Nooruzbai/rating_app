from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, VerifyEmail, \
    UserProfileRetrieveUpdateAPIView

app_name = 'accounts'

urlpatterns = [
    path('api/token/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/register/', UserRegistrationAPIView.as_view(), name='register' ),
    path('api/email_verify', VerifyEmail.as_view(), name='verify_email'),
    path('api/login/', UserLoginAPIView.as_view(), name="login-user"),
    path('api/logout/', UserLogoutAPIView.as_view(), name="logout-user"),

    # path('api/user_detail_view/', UserAPIView.as_view(), name="user-info"),
    path('api/user_detail_update_view/', UserProfileRetrieveUpdateAPIView.as_view(), name="user_profile_detail_update"),
    # path('api/user_profile_view/avatar/', UserAvatarAPIView.as_view(), name="user-avatar"),

]
