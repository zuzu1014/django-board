from django.core.management.base import BaseCommand, CommandError
from posts.models import Post
from accounts.models import User

class Command(BaseCommand):
    help = 'Populates the database. Deletes old entries'

    def handle(self, *args, **options):
        Post.objects.all().delete()
        print("done")