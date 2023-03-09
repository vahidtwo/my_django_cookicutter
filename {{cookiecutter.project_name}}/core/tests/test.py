from django.contrib.auth import get_user_model
from django.test import TransactionTestCase
from faker import Faker
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

User = get_user_model()


class TokenAPIClient(APIClient):
    def _set_token(self, user: User = None, user_id=None):
        if user is None:
            user = User.objects.get(user_id=user_id)
        token, _ = Token.objects.get_or_create(user=user)
        self.credentials(HTTP_AUTHORIZATION="token {}".format(token.key))

    def _remove_token(self):
        self.credentials()


class TokenAPITestCases(APITestCase, TransactionTestCase):
    client_class = TokenAPIClient
    fake = Faker(locale="fa_IR")

    def login(self, user: User = None):
        """
        Set user credentials
        """
        if user is None:
            self.client._set_token(user=self.user)
        else:
            self.client._set_token(user=user)

    def logout(self):
        """
        remove user credentials
        """
        self.client._remove_token()
