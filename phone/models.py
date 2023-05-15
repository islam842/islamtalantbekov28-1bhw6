from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=260)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title


