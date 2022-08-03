from .models import Post
from faker import Faker
from random import randint
from datetime import datetime


def create_posts(n=10):
    fake = Faker("pl_PL")
    for _ in range(n):
        created = fake.date_time()
        post = Post(
            title=fake.text(randint(10, 30)),
            content=fake.text(randint(100, 300)),
            created=created,
            modified=fake.date_time_between_dates(datetime_start=created, datetime_end=datetime.now()),
            published=fake.boolean(),
            sponsored=fake.boolean()
        )
        post.save()
