# djangito
<p align="center">

<a href="https://pypi.python.org/pypi/djangito">
<img src="https://img.shields.io/pypi/v/djangito.svg" /></a>
<a href="https://travis-ci.org/jamneck/djangito"><img src="https://travis-ci.org/jamneck/djangito.svg?branch=master" /></a>
</p>

Use AWS Application load balancer authentication with Cognito Hosted UI and Django

## Features
-   TODO

## Installation (not ready)
```
pip install djangito
```

## AWS Requirements
1. Please read https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html
2. Application load balancer with a listener for 443
3. An authentication rule for the login path (/alb/login*)

### Quick start
1. Add "djangito" to your INSTALLED_APPS setting like this::
```
INSTALLED_APPS = [
    ...
    'djangito',
]
```

2. Include the polls URLconf in your project urls.py like this::
```
    path('alb/', include('djangito.urls')),
```

Edit your settings.py file and add AutomaticUserLoginMiddleware to the MIDDLEWARE_CLASSES list, below the AuthenticationMiddleware:
```
MIDDLEWARE = [
  # 'django.contrib.auth.middleware.AuthenticationMiddleware',
  'authentication.middleware.AutomaticUserLoginMiddleware',
  # ...
]
```

Add the following settings to the settings.py file:
```
COGNITO_HOST = 'https://hosted.example.com'
COGNITO_CLIENT_ID = 'your_client_id'
COGNITO_REDIRECT_URI = 'https://www.example.com/login'
COGNITO_SCOPE = 'openid aws.cognito.signin.user.admin'
COGNITO_COOKIE = 'AWSELBAuthSessionCookie'
```



# Credits
This package was created with Cookiecutter and the `cs01/cookiecutter-pypackage` project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[cs01/cookiecutter-pypackage](https://github.com/cs01/cookiecutter-pypackage)
