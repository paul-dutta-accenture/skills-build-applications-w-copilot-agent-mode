from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data in safe order, one by one
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in User.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        yoga = Workout.objects.create(name='Yoga', description='Flexibility', difficulty='Easy')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], workout=pushups, duration_minutes=20, calories_burned=100)
        Activity.objects.create(user=users[1], workout=running, duration_minutes=30, calories_burned=250)
        Activity.objects.create(user=users[2], workout=yoga, duration_minutes=45, calories_burned=150)
        Activity.objects.create(user=users[3], workout=pushups, duration_minutes=15, calories_burned=80)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=350)
        Leaderboard.objects.create(team=dc, total_points=230)

        # Verification: print counts and sample documents
        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
        self.stdout.write(f"Users count: {User.objects.count()}")
        self.stdout.write(f"Teams count: {Team.objects.count()}")
        self.stdout.write(f"Workouts count: {Workout.objects.count()}")
        self.stdout.write(f"Activities count: {Activity.objects.count()}")
        self.stdout.write(f"Leaderboards count: {Leaderboard.objects.count()}")
        self.stdout.write(f"Sample User: {User.objects.first()}")
        self.stdout.write(f"Sample Team: {Team.objects.first()}")
        self.stdout.write(f"Sample Workout: {Workout.objects.first()}")
        self.stdout.write(f"Sample Activity: {Activity.objects.first()}")
        self.stdout.write(f"Sample Leaderboard: {Leaderboard.objects.first()}")
