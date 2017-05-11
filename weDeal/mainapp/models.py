from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Deal(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    description = models.TextField()
    total_price = models.IntegerField()
    number_of_items = models.IntegerField()
    ending_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    sold_items = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    @property
    def unit_price(self):
        return self.total_price / self.number_of_items

    @property
    def available_items(self):
        return self.number_of_items - self.sold_items

    @property
    def percentage_taken(self):
        return 100*self.sold_items / self.number_of_items

    @property
    def checked_stars_str(self):
        return '*' * self.rating

    @property
    def unchecked_stars_str(self):
        return '*' * (5 - self.rating)

    def __str__(self):
        return self.name
