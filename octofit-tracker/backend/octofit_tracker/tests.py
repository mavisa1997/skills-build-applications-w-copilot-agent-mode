from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class APIRootTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserTest(APITestCase):
	def test_create_user(self):
		url = reverse('user-list')
		data = {"name": "Test User", "email": "test@example.com", "team": "marvel"}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTest(APITestCase):
	def test_create_team(self):
		url = reverse('team-list')
		data = {"name": "avengers", "members": ["test@example.com"]}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTest(APITestCase):
	def test_create_activity(self):
		url = reverse('activity-list')
		data = {"user_email": "test@example.com", "activity": "run", "distance": 5}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTest(APITestCase):
	def test_create_leaderboard(self):
		url = reverse('leaderboard-list')
		data = {"team": "avengers", "points": 100}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTest(APITestCase):
	def test_create_workout(self):
		url = reverse('workout-list')
		data = {"user_email": "test@example.com", "workout": "push up", "reps": 20}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
