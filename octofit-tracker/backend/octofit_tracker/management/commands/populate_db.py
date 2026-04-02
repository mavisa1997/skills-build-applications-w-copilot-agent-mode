from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as octo_models

from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connessione diretta a MongoDB per operazioni avanzate
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Cancella dati esistenti
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Crea indici unici
        db.users.create_index([('email', 1)], unique=True)

        # Dati di esempio
        users = [
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
        ]
        teams = [
            {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com"]},
            {"name": "dc", "members": ["batman@dc.com", "superman@dc.com"]},
        ]
        activities = [
            {"user_email": "ironman@marvel.com", "activity": "run", "distance": 5},
            {"user_email": "cap@marvel.com", "activity": "cycle", "distance": 20},
            {"user_email": "batman@dc.com", "activity": "swim", "distance": 2},
            {"user_email": "superman@dc.com", "activity": "fly", "distance": 100},
        ]
        leaderboard = [
            {"team": "marvel", "points": 100},
            {"team": "dc", "points": 120},
        ]
        workouts = [
            {"user_email": "ironman@marvel.com", "workout": "bench press", "reps": 10},
            {"user_email": "cap@marvel.com", "workout": "push up", "reps": 50},
            {"user_email": "batman@dc.com", "workout": "pull up", "reps": 20},
            {"user_email": "superman@dc.com", "workout": "squat", "reps": 100},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database octofit_db popolato con dati di test!'))
