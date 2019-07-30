from django.db import models
from apps.core.models import TimestampedModel
# Create your models here.
class Profile(TimestampedModel):

    user = models.OneToOneField('authentication.User',on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True)

    #work_domain = models.CharField(max_length=50)

    follows = models.ManyToManyField('self',symmetrical=False,related_name='followed_by')

    favorites = models.ManyToManyField('events.Event',related_name='favorited_by')

    def __str__(self):
        return self.user.email

    def follow(self,profile):

        self.follows.add(profile)

    def unfollow(self,profile):

        self.follows.remove(profile)

    def is_following(self,profile):

        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self,profile):

        return self.is_followed_by.filter(pk=profile.pk).exists()

    def favorite(self,event):

        self.favorite.add(event)

    def unfavorite(self,event):

        self.unfavorite.remove(event)
    
    def has_favorited(self,event):
        return self.favorites.filter(pk=event.pk).exists()
    
