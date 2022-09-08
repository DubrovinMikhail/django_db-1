from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=250)
    price = models.IntegerField()
    release_date = models.DateTimeField(max_length=100)
    lte_exists = models.BooleanField(max_length=10)
    slug = models.SlugField(max_length=50)
