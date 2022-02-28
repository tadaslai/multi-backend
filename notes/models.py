from django.db import models


# Create your models here.
class Note(models.Model):
    id = models.BigAutoField(auto_created=True, unique=True, primary_key=True, serialize=True, verbose_name='ID')
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.description


class User(models.Model):
    id = models.BigAutoField(auto_created=True, unique=True, primary_key=True, serialize=True, verbose_name='ID')
    username = models.CharField(max_length=20)
    password = models.DateField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.username
