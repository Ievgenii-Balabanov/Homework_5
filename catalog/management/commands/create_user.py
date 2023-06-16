from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("new_user", type=int,
                            help="Add a \"new_user\" ", choices=range(1, 11))

    def handle(self, *args, **options):
        faker = Faker()
        User.objects.bulk_create(
            (User(username=faker.name(),
                  email=faker.email(),
                  password=faker.password())
             for _ in range(options.get("new_user"))))
        self.stdout.write(self.style.SUCCESS(f"New User number: {options.get('new_user')}"))
