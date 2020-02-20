from django.urls import path

from djangito import views


urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(),
        name='alb_login'
    ),

    path(
        'signup/',
        views.SignupView.as_view(),
        name='alb_signup'
    ),

    path(
        'logout/',
        views.LogoutView.as_view(),
        name='alb_logout',
    ),

    path(
        'forgot-password/',
        views.ForgotPasswordView.as_view(),
        name='alb_forgot_password',
    )
]
