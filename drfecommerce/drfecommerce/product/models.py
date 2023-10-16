from django.db import models
from mptt.models import MPTTMpodel, TreeForeignKey


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = Tree


class Brand(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
