from django.db import models
from django.utils import timezone

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=64)
    date_of_birth = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s (%s)" % (self.name, self.date_of_birth)

class Speech(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, on_delete=models.PROTECT)
    body = models.TextField()
    link = models.URLField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.speaker.name)        