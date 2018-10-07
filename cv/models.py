from django.db import models

class CVSection(models.Model):
    section_title = models.CharField(max_length=100, blank=True, null=True)
    section_sequence = models.PositiveSmallIntegerField()
    section_body = models.TextField()
    section_start_date = models.DateField(blank=True, null=True)
    section_end_date = models.DateField(blank=True, null=True)
    date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return 'Section {0}'.format(self.section_sequence)
