from django.contrib.auth.models import User

from django_seed import Seed


seeder = Seed.seeder()

seeder.add_entity(User, 1, {
    'username': 'admin',
    'password': '123password123'
})
