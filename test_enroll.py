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
        self.assertFalse(self.enroll.check_username_valid("          "))
        self.assertFalse(self.enroll.check_username_valid(""))

    def test_check_password_valid(self):
        self.assertTrue(self.enroll.check_password_valid("GoodPassword-9256"))
        self.assertTrue(self.enroll.check_password_valid("AnotherGoodPassword1622!@"))
        self.assertTrue(self.enroll.check_password_valid("sz2nzmTMsxADrhG2H9fusS3ZwMUgRrWRpbrqdPPhWbndMGQGTb"))
        self.assertFalse(self.enroll.check_password_valid("123456789"))
        self.assertFalse(self.enroll.check_password_valid("123456789"))
        self.assertFalse(self.enroll.check_password_valid("terrifically"))
        self.assertFalse(self.enroll.check_password_valid("terrifically1234"))
        self.assertFalse(self.enroll.check_password_valid("1234terrifically"))

    def test_check_for_user(self):
        self.assertFalse(self.enroll.check_for_user("username"))
        self.assertTrue(self.enroll.check_for_user("gloomyjim"))

    def test_enroll_user(self):
        self.assertTrue(self.enroll.enroll_user("goodusername", "goodpassword123"))
