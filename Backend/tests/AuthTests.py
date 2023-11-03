import unittest

from Backend.secrets.API_KEYS import API_KEYS


class AuthTests(unittest.TestCase):
    def test_bearer_token_generation(self):
        api_keys = API_KEYS()
        self.assertTrue(len(api_keys.bearer_token) > 0)


if __name__ == '__main__':
    unittest.main()
