import unittest
from app.app import Usercredentials
from unittest import TestCase


class Testsignup(unittest.TestCase):
    def setup():
        self.Usercredentials = Usercredentials()

    def test_full_name(self):
        name = Usercredentials('naome', 'noma','706074507', 'naomenoma@gmail.com')
        self.assertEqual(name.fullname(), 'naome  noma')

    def test_validate_email_returns_email(self):
        signup = Usercredentials.isValidEmail('naome@gmail.com')
        self.assertEqual(signup, 'naome@gmail.com')




if __name__ == '__main__':
    unittest.setup()


    
