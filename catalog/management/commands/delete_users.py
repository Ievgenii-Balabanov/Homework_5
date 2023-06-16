from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("user_id", nargs="+", type=int, help="User ID")

    def handle(self, *args, **options):
        user_queryset = User.objects.filter(id__in=options.get("user_id"))
        if user_queryset.filter(is_superuser=True).exists():
            self.stdout.write(self.style.ERROR("ERROR: Superuser can't be deleted"))
        else:
            user_queryset.delete()
            self.stdout.write(self.style.SUCCESS("User successfully deleted"))

        # ---------------------------------------------------------------

        """
        implementation using "for" loops
        """

        # for user_id in options["user_id"]:
        #     if User.objects.filter(pk=user_id).filter(is_superuser=True).exists():
        #         return self.stdout.write(self.style.ERROR("ERROR: Superuser can't be deleted"))
        #     else:
        #         User.objects.filter(pk=user_id).delete()
        #         return self.stdout.write(self.style.SUCCESS("Object successfully deleted"))
        # # else:
        # #     return self.stdout.write(self.style.ERROR("ERROR: Object with specified ID doesn't exist"))
