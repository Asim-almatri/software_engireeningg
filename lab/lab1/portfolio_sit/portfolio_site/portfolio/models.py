from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
