import base64
import json

import jwt
import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


USER_MODEL = get_user_model()


class ALBAuth(ModelBackend):

    def authenticate(self, request, **kwargs):
        if request:
            self.encoded_jwt = request.META.get('HTTP_X_AMZN_OIDC_DATA')
            if self.encoded_jwt:
                self.payload = self.decode_alb_jwt()
                return self.get_or_create_for_alb()

    def decode_alb_jwt(self):
        # Step 1: Get the key id from JWT headers (the kid field)
        jwt_headers = self.encoded_jwt.split('.')[0]
        decoded_jwt_headers = base64.b64decode(jwt_headers)
        decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")
        decoded_json = json.loads(decoded_jwt_headers)
        kid = decoded_json['kid']

        # Step 2: Get the public key from regional endpoint
        url = f'https://public-keys.auth.elb.us-east-1.amazonaws.com/{kid}'
        req = requests.get(url)
        pub_key = req.text

        # Step 3: Get the payload
        return jwt.decode(
            self.encoded_jwt,
            pub_key,
            algorithms=['ES256']
        )

    def get_or_create_for_alb(self):
        user_info = {'username': self.payload['sub'][:150]}
        if 'given_name' in self.payload:
            user_info['first_name'] = self.payload['given_name'][:30]
        elif 'name' in self.payload:
            user_info['first_name'] = self.payload['name'][:30]
        if 'family_name' in self.payload:
            user_info['last_name'] = self.payload['family_name'][:30]

        self.user, created = USER_MODEL.objects.get_or_create(
            email=self.payload['email'],
            defaults=user_info
        )

        if created:
            self.setup_user_profile()

        return self.user

    def setup_user_profile(self):
        pass
