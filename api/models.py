from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=100)
    parent_category = models.CharField(max_length=100)

    class Meta:
        db_table = 'Category'

class Product(models.Model):
    product_name = models.CharField(unique=True, max_length=100)
    price = models.IntegerField()
    categories = models.CharField(max_length=500)

    class Meta:
        db_table = 'Product'