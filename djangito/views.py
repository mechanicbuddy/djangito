from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import generic as generic_views


class LoginView(generic_views.View):
    """
    Return the user-originating redirect URL if it's safe.
    """

    def get(self, request, *args, **kwargs):
        next_url = self.request.GET.get('next')

        if next_url and next_url.startswith('/'):
            redirect_to = next_url
        else:
            redirect_to = settings.LOGIN_REDIRECT_URL

        response = redirect(redirect_to, permanent=False)

        response.set_cookie(
            'alb-django-guard',
            'load'
        )
        return response


class LogoutView(generic_views.View):

    def get(self, request, *args, **kwargs):
        logout(request)

        response = redirect(
            '{}/logout?client_id={}&response_type=code&redirect_uri={}&scope={}'.format(
                settings.COGNITO_HOST,
                settings.COGNITO_CLIENT_ID,
                settings.COGNITO_REDIRECT_URI,
                settings.COGNITO_SCOPE
            )
        )
        response.set_cookie(
            f'{settings.COGNITO_COOKIE}-0',
            secure=True,
            httponly=True,
            max_age=-1
        )
        response.set_cookie(
            f'{settings.COGNITO_COOKIE}-1',
            secure=True,
            httponly=True,
            max_age=-1
        )
        # set the expiration time of the authentication session cookie to -1
        response.set_cookie(
            'alb-django-guard',
            'redirect'
        )

        return response


class SignupView(generic_views.View):
    """
    Redirect to login if authenticated. Otherwise redirect to Cognito
    """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('alb_login')

        redirect_to = '{}/signup?client_id={}&response_type=code&redirect_uri={}&scope={}'.format(
                settings.COGNITO_HOST,
                settings.COGNITO_CLIENT_ID,
                settings.COGNITO_REDIRECT_URI,
                settings.COGNITO_SCOPE
            )

        return redirect(redirect_to, permanent=False)


class ForgotPasswordView(generic_views.View):
    """
    Redirect to forgot password view on cognito
    """

    def get(self, request, *args, **kwargs):

        redirect_to = '{}/forgotPassword?client_id={}&response_type=code&redirect_uri={}&scope={}'.format(
                settings.COGNITO_HOST,
                settings.COGNITO_CLIENT_ID,
                settings.COGNITO_REDIRECT_URI,
                settings.COGNITO_SCOPE
            )

        return redirect(redirect_to, permanent=False)
