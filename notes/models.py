from django.db import models

class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_body = models.TextField()
    category = models.CharField(max_length=100)
    date_submitted = models.DateField(auto_now_add=True)
    date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return '{0}-{1}'.format(self.category, self.note_title)
