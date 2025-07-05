# from django.contrib.auth import get_user_model
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse

# User = get_user_model()

# class SignUpViewTest(APITestCase):
#     def setUp(self):
#         # If you have a named URL pattern for signup, use reverse
#         # For example: reverse('signup')
#         self.signup_url = '/api/signup/'  # adjust this to your real endpoint

#     def test_signup_creates_user(self):
#         data = {
#             "username": "testuser",
#             "email": "testuser@example.com",
#             "password": "strongpassword123",
#             "first_name": "Test",
#             "last_name": "User"
#         }

#         response = self.client.post(self.signup_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # Check the user exists in the database
#         user = User.objects.get(username='testuser')
#         self.assertIsNotNone(user)
#         self.assertEqual(user.email, "testuser@example.com")
#         self.assertTrue(user.check_password("strongpassword123"))

#     def test_signup_missing_required_field(self):
#         data = {
#             "email": "testuser2@example.com",
#             "password": "somepassword"
#             # Missing username
#         }

#         response = self.client.post(self.signup_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('username', response.data)

#     def test_signup_existing_username(self):
#         # Create a user first
#         User.objects.create_user(username='testuser', email='existing@example.com', password='password')

#         data = {
#             "username": "testuser",
#             "email": "newemail@example.com",
#             "password": "newpassword"
#         }

#         response = self.client.post(self.signup_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('username', response.data)