import unittest
from app.services.user_service import authenticate
from app.models.user_models import RegularUser, PremiumUser, AdminUser

class TestUserService(unittest.TestCase):
    def test_authenticate_success(self):
        # hardcoded users in user_service.py
        user = authenticate("admin", "123456")
        self.assertIsNotNone(user)
        self.assertEqual(user.get_role(), "Admin")

    def test_authenticate_fail(self):
        user = authenticate("admin", "wrongpass")
        self.assertIsNone(user)

    def test_roles(self):
        regular = RegularUser("regular")
        premium = PremiumUser("premium")
        admin = AdminUser("admin")
        self.assertEqual(regular.get_role(), "Regular")
        self.assertEqual(premium.get_role(), "Premium")
        self.assertEqual(admin.get_role(), "Admin")

if __name__ == "__main__":
    unittest.main()
