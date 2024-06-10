from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True,blank=True, null=True)
