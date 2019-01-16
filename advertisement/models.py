from django.db import models

from customers.models import Customer


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '<City: {}>'.format(self.name)


class Advertisement(models.Model):
    ORDER_TYPE = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )

    title = models.CharField(max_length=200)
    date_publication = models.DateField()
    description = models.TextField()
    unique_views = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_type = models.CharField(
        max_length=4, choices=ORDER_TYPE, default='sell'
    )

    def __str__(self):
        return '<Ad: {} {}>'.format(self.date_publication, self.title)
