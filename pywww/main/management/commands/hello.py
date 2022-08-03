from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Writes greetings"

    def handle(self, *args, **options):
        self.stdout.write("Hello World")
        
    def add_arguments(self, parser):
        pass