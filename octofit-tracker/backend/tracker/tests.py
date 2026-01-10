
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
	def test_create_user(self):
		team = Team.objects.create(name="Marvel")
		user = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=team)
		self.assertEqual(user.name, "Spider-Man")

class TeamModelTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name="DC")
		self.assertEqual(team.name, "DC")

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		workout = Workout.objects.create(name="Pushups", description="Upper body", difficulty="Easy")
		self.assertEqual(workout.name, "Pushups")

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		team = Team.objects.create(name="Marvel")
		user = User.objects.create(name="Iron Man", email="ironman@marvel.com", team=team)
		workout = Workout.objects.create(name="Running", description="Cardio", difficulty="Medium")
		activity = Activity.objects.create(user=user, workout=workout, duration_minutes=30, calories_burned=300)
		self.assertEqual(activity.user.name, "Iron Man")

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		team = Team.objects.create(name="Marvel")
		leaderboard = Leaderboard.objects.create(team=team, total_points=100)
		self.assertEqual(leaderboard.total_points, 100)
