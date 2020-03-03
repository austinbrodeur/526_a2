from unittest import TestCase
from authenticate import Authenticate


class TestAuthenticate(TestCase):
    authenticate = Authenticate()

    def test_auth_user(self):
        self.assertTrue(self.authenticate.auth_user("goodusername", "goodpassword123"))