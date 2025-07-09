from django.urls import path, include
from .views import SignUpView, ProfileView, ChangePasswordView
from dj_rest_auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # Signup
    path('signup/', SignUpView.as_view(), name='signup'),

    # Login / Logout
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),

    # Password Management
    path('password/change/', ChangePasswordView.as_view(), name='password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # JWT
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
]