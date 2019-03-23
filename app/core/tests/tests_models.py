from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creation of user via an email succesful"""

        email = 'example@blabla.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalized(self):
        """normalized user's email"""
        email = 'emaple@BLABLA.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='123456'
        )
        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """Test invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_super_user(self):
        """the creation of superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
