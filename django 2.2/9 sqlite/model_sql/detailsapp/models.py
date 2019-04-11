from django.db import models
class UserDetails(models.Model):
    title = models.CharField(max_length=100)
    gender = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    def __str__(self):
        return self.title
