from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CartoonUser(models.Model):
    username = models.CharField(max_length=25)
    surname = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Cartoon user: {self.username}, Surname: {self.surname}, Email: {self.email}"


class Cartoon(models.Model):
    USA = 'US'
    EUROPE = 'EU'
    UKRAINE = 'UA'
    COUNTRY_CHOICES = [
        (USA, 'America'),
        (EUROPE, 'Europe'),
        (UKRAINE, 'Ukraine')
    ]
    user = models.ForeignKey(CartoonUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20, default='default')
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='O')
    year = models.PositiveIntegerField(default=1900, validators=[MinValueValidator(1901),
                                                                 MaxValueValidator(2025)])
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1),
                                                                MaxValueValidator(100)])

    def __str__(self):
        return f"Cartoon: {self.title}, Author: {self.author}, Year: {self.year}, Rating: {self.rating}"
