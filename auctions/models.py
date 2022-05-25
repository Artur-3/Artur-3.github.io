from cgi import print_exception
from distutils.command.upload import upload
from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    photo = models.ImageField(upload_to='auctions/static/media/img')
    price = models.IntegerField()
    clas = models.ForeignKey(Category, blank=True, on_delete=models.PROTECT, related_name="nature")

    def __str__(self):
        return f"{self.name}"