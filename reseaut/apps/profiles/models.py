from django.db import models
from apps.core.models import TimestampedModel
# Create your models here.
class Profile(TimestampedModel):

    user = models.OneToOneField('authentication.User',on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    #work_domain = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email


