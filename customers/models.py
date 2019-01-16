from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('none', 'Не указано'),
    )
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, default='none'
    )
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '<Customer: {} {}>'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return self.get_full_name()
