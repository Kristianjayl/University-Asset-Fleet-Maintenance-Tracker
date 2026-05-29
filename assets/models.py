from django.db import models
from django.conf import settings

# Create your models here.

class AssetCategory(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name        = 'Asset Category'
        verbose_name_plural = 'Asset Categories'
        ordering            = ['name']

    def __str__(self):
        return self.name