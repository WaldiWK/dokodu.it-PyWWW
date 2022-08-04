from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    aviable = models.BooleanField(default=True)
    publication_year=models.PositiveIntegerField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.id} {self.title} aviable: {self.aviable}")

