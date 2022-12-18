from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Songs(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    titleRom = models.CharField(max_length=120, blank=True)
    song = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    opedin = models.CharField(max_length=40)
    video = models.URLField(max_length=120, blank=True)
    audio = models.URLField(max_length=120, blank=True)

    def __str__(self):
        return """Song: %s | Artist: %s | Show: %s | Type: %s
        """%(self.song, self.artist, self.titleRom, self.opedin)



