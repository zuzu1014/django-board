from django.core.management.base import BaseCommand, CommandError
from z.models import Post
from accounts.models import User

class Command(BaseCommand):
    help = 'Populates the database. Deletes old entries'

    def handle(self, *args, **options):
        print("Populating...")
        for i in range(300):
            Post.objects.create(author=User.objects.get(is_active=True),title="이것은 테스트용 글입니다. "+str(i),content="이것은 테스트용 글 내용입니다!!")
        print("Done.")