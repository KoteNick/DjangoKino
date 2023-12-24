from django.db import models
from django.core import validators

class Film(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    time = models.TimeField()
    timeEnd = models.TimeField()
    hall = models.IntegerField()
    price = models.IntegerField(default=100)
    def __str__(self):
        return self.title[:10]

class Hall(models.Model):
    number = models.IntegerField()
    seats = models.CharField(validators=[validators.int_list_validator()], max_length=300, blank=True,  null=True)
    def __str__(self):
        return f"Hall {self.number}"
