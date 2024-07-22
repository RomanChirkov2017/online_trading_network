from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Создание суперпользователя. """

    def handle(self, *args, **options):
        user = User.objects.create(email="Admin@sky.pro")
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password("qwe123")
        user.save()
