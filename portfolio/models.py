from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200, blank=False)
    screenshot = models.ImageField()
    frontend_url = models.URLField()
    code_url = models.URLField()
    description = models.TextField()
    technology = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True, blank=True)

    # Convert this to a list to facilitate looping to render logos in the template
    def technology_list(self):
        return self.technology.split(',')

    def __str__(self):
        return '{0}'.format(self.title)
