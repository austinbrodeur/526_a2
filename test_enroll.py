from unittest import TestCase
from enroll import Enroll


class TestEnroll(TestCase):
    enroll = Enroll()

    def test_check_username_valid(self):
        """
        This test checks various usernames to ensure they're being properly checked.
        """
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
        """
        This test checks various passwords to ensure they're being properly checked.
        """
        self.assertTrue(self.enroll.check_password_valid("GoodPassword-9256"))
        self.assertTrue(self.enroll.check_password_valid("AnotherGoodPassword1622!@"))
        self.assertTrue(self.enroll.check_password_valid("sz2nzmTMsxADrhG2H9fusS3ZwMUgRrWRpbrqdPPhWbndMGQGTb"))
        self.assertFalse(self.enroll.check_password_valid("123456789"))
        self.assertFalse(self.enroll.check_password_valid("123456789"))
        self.assertFalse(self.enroll.check_password_valid("terrifically"))
        self.assertFalse(self.enroll.check_password_valid("terrifically1234"))
        self.assertFalse(self.enroll.check_password_valid("1234terrifically"))

    def test_check_for_user(self):
        """
        Precondition: goodusername already exists in users.txt.
        This test ensures existing users are checked for properly.
        """
        self.assertTrue(self.enroll.check_for_user("goodusername")) # should be enrolled
        self.assertFalse(self.enroll.check_for_user("notinuseusername")) # should not be enrolled
        self.assertFalse(self.enroll.check_for_user("\n")) # to ensure added newline doesn't improperly get checked

    def test_enroll_user(self):
        """
        Precondition: this test assumes the users.txt file is empty. Should fail if 'goodusername' is already in use.
        This test ensures the correct exit codes are thrown when a username is accepted/rejected.
        """
        with self.assertRaises(SystemExit) as cm:
            self.enroll.enroll_user("goodusername", "goodpassword123")
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm: # because the same user has been enrolled above, this should reject
            self.enroll.enroll_user("goodusername", "goodpassword123")
        self.assertEqual(cm.exception.code, -1)
        with self.assertRaises(SystemExit) as cm:
            self.enroll.enroll_user("alsoagooduser", "anothergoodpassword123")
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm: # different username with same password to ensure hashing/salting
            # is working correctly
            self.enroll.enroll_user("alsoagooduser2", "anothergoodpassword123")
        self.assertEqual(cm.exception.code, 0)
