# Python
import unittest
from password_checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak_passwords(self):
        self.assertEqual(check_password_strength("abc"), "弱")  # too short, only lowercase
        self.assertEqual(check_password_strength("1234567"), "弱")  # only digits, too short
        self.assertEqual(check_password_strength("ABCDEFG"), "弱")  # only uppercase, too short
        self.assertEqual(check_password_strength("!!!!!!!"), "弱")  # only special chars, too short
        self.assertEqual(check_password_strength(""), "弱")  # empty string

    def test_medium_passwords(self):
        self.assertEqual(check_password_strength("abc12345"), "中等")  # no uppercase, no special
        self.assertEqual(check_password_strength("ABC12345"), "中等")  # no lowercase, no special
        self.assertEqual(check_password_strength("Abcdefgh"), "中等")  # no digit, no special
        self.assertEqual(check_password_strength("Abc12345"), "中等")  # no special
        self.assertEqual(check_password_strength("Abc!@#$%"), "中等")  # no digit

    def test_strong_passwords(self):
        self.assertEqual(check_password_strength("Abc12345!"), "強")  # all rules
        self.assertEqual(check_password_strength("A1b2c3d4!"), "強")  # all rules
        self.assertEqual(check_password_strength("Password1!"), "強")  # all rules

    def test_edge_cases(self):
        # Test minimum length for medium/strong
        self.assertEqual(check_password_strength("A1b2c3d4"), "中等")  # no special, exactly 8 chars
        self.assertEqual(check_password_strength("A1!bcdef"), "強")    # all rules, exactly 8 chars

        # Test only one character type, but long enough
        self.assertEqual(check_password_strength("12345678"), "弱")  # only digits, long enough
        self.assertEqual(check_password_strength("abcdefgh"), "弱")  # only lowercase, long enough
        self.assertEqual(check_password_strength("ABCDEFGH"), "弱")  # only uppercase, long enough
        self.assertEqual(check_password_strength("!@#$%^&*"), "弱")  # only special chars, long enough

        # Test empty string and very short passwords
        self.assertEqual(check_password_strength(""), "弱")
        self.assertEqual(check_password_strength("a"), "弱")
        self.assertEqual(check_password_strength("A"), "弱")
        self.assertEqual(check_password_strength("1"), "弱")
        self.assertEqual(check_password_strength("!"), "弱")

        # Test borderline cases for strong passwords
        self.assertEqual(check_password_strength("Abc123!@"), "強")  # all rules, exactly 8 chars
        self.assertEqual(check_password_strength("Abc123!"), "中等")  # missing one char for length

        # Test unicode/special characters
        self.assertEqual(check_password_strength("密码123!A"), "中等")  # contains unicode, all rules
        self.assertEqual(check_password_strength("A1b2c3d4"), "中等")  # no special
        self.assertEqual(check_password_strength("A1!bcdef"), "強")  # exactly 8 chars, all rules
        self.assertEqual(check_password_strength("12345678"), "弱")  # only digits, long enough
        self.assertEqual(check_password_strength("abcdefgh"), "弱")  # only lowercase, long enough
        self.assertEqual(check_password_strength("ABCDEFGH"), "弱")  # only uppercase, long enough
        self.assertEqual(check_password_strength("!@#$%^&*"), "弱")  # only special chars, long enough

if __name__ == "__main__":
    unittest.main()