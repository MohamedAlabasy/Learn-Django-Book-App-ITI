from django.db import models
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=250)
    details = models.CharField(max_length=250, null=True)
    image = models.URLField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250)
    summary = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.URLField()
    add_to_site = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    appropriate = models.CharField(max_length=250, choices=[(
        "und", "under 18"), ("ad", "Adults")], default="ad")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        # return str(self.item) + ": $" + str(self.price)
        return self.name
