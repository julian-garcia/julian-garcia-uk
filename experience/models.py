from django.db import models

class Experience(models.Model):
    class Meta:
        verbose_name_plural = 'Experience'

    position = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{0} from {1}'.format(self.position, self.start_date)
