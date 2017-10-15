import unittest
from app.auth import Auth


class TddPythonLab(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()

    def test_auth_success(self):
        result = self.auth.check_user(login='user', password='password')
        self.assertEqual(1, result)

    def test_auth_error_user_not_found(self):
        result = self.auth.check_user(login='user_ghost', password='password')
        self.assertEqual(2, result)

    def test_auth_error_password_error(self):
        result = self.auth.check_user(login='user', password='password_error')
        self.assertEqual(3, result)

    def test_create_user_success(self):
        result = self.auth.add_user(login='user2', password='password2')
        self.assertEqual(0, result)

    def test_create_user_failed(self):
        result = self.auth.add_user(login='user_new', password='password_new')
        self.assertEqual(1, result)

    def test_create_user_failed_login_is_null(self):
        result = self.auth.add_user(login=None, password='password_new')
        self.assertEqual(1, result)

    def test_create_user_failed_password_is_null(self):
        result = self.auth.add_user(login='user_new', password=None)
        self.assertEqual(1, result)

    def test_delete_user_success(self):
        result = self.auth.del_user(login='user2', password='password2')
        self.assertEqual(0, result)

    def test_delete_user_failed(self):
        result = self.auth.del_user(login='user_new', password='password_failed')
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
