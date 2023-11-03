import unittest
from handlers.authentication import LoginHandler


class TestLoginHandler(unittest.TestCase):
    def test_basic_handler(self):
        test_login_handler = LoginHandler()
        self.assertTrue(test_login_handler.validate_user("test", "test"))


if __name__ == '__main__':
    unittest.main()
