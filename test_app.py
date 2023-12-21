# test_app.py

import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Devfest', response.data)

if __name__ == '__main__':
    unittest.main()
