from books.models import Book
from faker import Faker

fake = Faker()

def create_books(n=10):
    result = []
    for i in range(n):
        book = Book.objects.create(
            title=fake.text(fake.random.randint(20,80)),
            description=fake.text(fake.random.randint(200,800)),
            aviable=fake.boolean(),
            publication_year=int(fake.year()),
            author=fake.name()
        )
        result.append(book)
    return result

