"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model #get default user model to be referenced directly

class ModelTests(TestCase):
    """ Test creating a user with email is succesful"""

    email = "test@example.com"
    password = 'testpass123'
    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(check_password(password))
