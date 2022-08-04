from django.core.management.base import BaseCommand
from books.utils import create_books


class Command(BaseCommand):
    help = "Add sample fake books to library"

    def handle(self, *args, **options):
        amount = options.get("number", 10)
        books = create_books(amount)
        self.stdout.write(f"{len(books)} books was created!!")

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            default=10,
            dest="number",
            help="|Amount of books"
        )
