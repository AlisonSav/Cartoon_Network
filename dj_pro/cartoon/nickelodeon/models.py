from django.db import models


class CartoonUser(models.Model):
    username = models.CharField(max_length=25)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f"Cartoon user: {self.username}, Pwd: {self.surname}"


class Cartoon(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20, default='default')
    year = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Cartoon: {self.title}, Author: {self.author}, Year: {self.year}, Rating: {self.rating}"
