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

    @property
    def unit_price(self):
        return self.total_price / self.number_of_items

