from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address

class Contact(models.Model):
    phone = models.PositiveSmallIntegerField()


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.ForeignKey(Contact, on_delete=models.CASCADE)
