"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model #get default user model to be referenced directly

class ModelTests(TestCase):
    """ Test creating a user with email is succesful"""
    def test_create_user_with_email_successful(self):
        email = "test1@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        ''' Test email is normalized for new user'''
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
    def test_new_user_without_email_raises_error(self):
        ''' Test creating user without email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_super_user(self):
        """ Test to create a super user"""
        user = get_user_model().objects.create_superuser(
            'test1@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)




