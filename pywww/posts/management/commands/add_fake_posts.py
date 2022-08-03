from django.core.management.base import BaseCommand
from posts.utils import create_posts

class Command(BaseCommand):
    help = "Add sample posts"

    def add_arguments(self, parser):
        parser.add_argument(
            '-c', 
            '--count',
            type=int, required=True, dest="count", 
            help="Amount of posts"
        )

    def handle(self,*args, **options):
        create_posts(options.get("count"))
        self.stdout.write('Post has been created')

