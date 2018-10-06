from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_postcode = models.CharField(max_length=20)
    event_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.event_name
