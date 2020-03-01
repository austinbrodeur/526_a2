from unittest import TestCase
from enroll import Enroll

class TestEnroll(TestCase):

    enroll = Enroll()

    def test_check_username_valid(self):
        self.assertTrue(self.enroll.check_username_valid("username"))
        self.assertTrue(self.enroll.check_username_valid("user_name123"))
        self.assertTrue(self.enroll.check_username_valid("12345"))
        self.assertTrue(self.enroll.check_username_valid("123456789012345"))
        self.assertFalse(self.enroll.check_username_valid("username123@"))
        self.assertFalse(self.enroll.check_username_valid("username123ﷺ"))
        self.assertFalse(self.enroll.check_username_valid("1234"))
        self.assertFalse(self.enroll.check_username_valid("waaaaaaaaaaaaaaaaaaaaaaaaaaaytoolong"))


    def test_check_password_valid(self):
        self.assertTrue(self.enroll.check_password_valid("Goodpassword-9256"))
        self.assertTrue(self.enroll.check_password_valid("Goodpassword-9256"))
        self.assertFalse(self.enroll.check_password_valid("123456789"))
        self.assertFalse(self.enroll.check_password_valid("123456789"))
