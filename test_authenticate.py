from unittest import TestCase
from authenticate import Authenticate


class TestAuthenticate(TestCase):
    authenticate = Authenticate()

    def test_auth_user(self):
        """
        Precondition: assumes test_enroll_user from test_enroll has already been run.
        """
        self.assertTrue(self.authenticate.auth_user("goodusername", "goodpassword123"))
        self.assertFalse(self.authenticate.auth_user("goodusername", "badpass123")) # wrong pass
        self.assertFalse(self.authenticate.auth_user("goodusername", ""))
        self.assertFalse(self.authenticate.auth_user("", "goodpassword123"))
        self.assertTrue(self.authenticate.auth_user("alsoagooduser", "anothergoodpassword123")) # test different
        # users with same pass
        self.assertTrue(self.authenticate.auth_user("alsoagooduser2", "anothergoodpassword123"))
        self.assertFalse(self.authenticate.auth_user("", "anothergoodpassword123")) # blank user
        self.assertFalse(self.authenticate.auth_user("alsoagooduser", "goodpassword123")) # different users with a
        # good password but for a different user
        self.assertFalse(self.authenticate.auth_user("alsoagooduser2", "goodpassword123"))
