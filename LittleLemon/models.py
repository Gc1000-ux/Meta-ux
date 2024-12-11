from django.db import models


# Create your models here.
class Menu(models.Model):
    menu_identity = models.IntegerField(5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)

    def __str__(self):
      return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    booking_identity = models.IntegerField(11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    bookingDate = models.DateField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
