from django.db import models

class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(blank=False)

    def __str__(self):
        return self.Title