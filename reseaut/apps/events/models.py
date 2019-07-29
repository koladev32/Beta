from django.db import models
from apps.core.models import TimestampedModel
# Create your models here.

class Event(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255,unique=True)

    event_name = models.CharField(db_index=True,max_length=255)

    location = models.CharField(max_length=255)

    event_date = models.DateField(auto_now_add=True)

    event_time = models.TimeField(auto_now_add=True)

    description = models.TextField()

    image = models.URLField(max_length=200,blank=True)

    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE,related_name='events')

    def __str__(self):
        return self.event_name
    