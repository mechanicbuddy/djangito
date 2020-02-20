from django.contrib import auth
from django.contrib.auth.middleware import MiddlewareMixin


class AutomaticUserLoginMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not AutomaticUserLoginMiddleware._is_user_authenticated(request):
            user = auth.authenticate(request)
            if user:
                request.user = user
                auth.login(request, user)

    @staticmethod
    def _is_user_authenticated(request):
        user = request.user
        return user and user.is_authenticated
