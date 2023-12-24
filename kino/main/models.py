from django.db import models
from django.core import validators
from datetime import datetime

class Film(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    time = models.TimeField()
    timeEnd = models.TimeField()
    hall = models.IntegerField()
    price = models.IntegerField(default=100)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title[:10]
    @property
    def in_progress(self):
        ti = datetime.now().time()
        return (ti > self.time and ti < self.timeEnd)

class Hall(models.Model):
    number = models.IntegerField()
    seats = models.CharField(validators=[validators.int_list_validator()], max_length=300, default='0')
    in_use = models.BooleanField(default=False)
    def __str__(self):
        return f"Hall {self.number}"
