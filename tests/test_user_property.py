import unittest
from app.models.user_models import RegularUser, PremiumUser, AdminUser

class TestUserProperty(unittest.TestCase):
    def test_username_property_validation(self):
         # rast valid
        u = RegularUser("nina")
        self.assertEqual(u.username, "nina")

        # rast invalid: username < 3 chars
        with self.assertRaises(ValueError):
            u.username = "a"   # setter duhet me qit ValueError

        # rast invalid direkt ne konstruktor
        with self.assertRaises(ValueError):
            RegularUser("ab")

    def test_roles(self):
        self.assertEqual(RegularUser("nina").get_role(), "Regular")
        self.assertEqual(PremiumUser("qendresa").get_role(), "Premium")
        self.assertEqual(AdminUser("admini").get_role(), "Admin")

if __name__ == "__main__":
    unittest.main()
