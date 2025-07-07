from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from authentications.models import User
from events.models import Events

class EventsViewSetTestCase(APITestCase):
    def setUp(self):
        # Create users
        self.admin_user = User.objects.create_user(username='adminuser', email='admin@example.com', password='password123', is_staff=True)
        self.team_member_user = User.objects.create_user(username='teammember', email='teammember@example.com', password='password123')
        self.other_user = User.objects.create_user(username='otheruser', email='other@example.com', password='password123')

        # Create an event
        self.event = Events.objects.create(admin=self.admin_user, title='Test Event')
        self.event.team_members.add(self.team_member_user)

        self.url = reverse('events-list')

    def test_admin_can_list_event(self):
        """
        Ensure admin user can list the event.
        """
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.event.title)

    def test_team_member_can_list_event(self):
        """
        Ensure team member can list the event.
        """
        self.client.force_authenticate(user=self.team_member_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.event.title)

    def test_other_user_cannot_list_event(self):
        """
        Ensure a user not associated with the event cannot list it.
        """
        self.client.force_authenticate(user=self.other_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_unauthenticated_user_cannot_list_events(self):
        """
        Ensure unauthenticated users cannot list events.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
