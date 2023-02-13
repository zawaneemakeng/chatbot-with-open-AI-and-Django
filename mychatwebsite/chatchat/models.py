from django.db import models

# Create your models here.


class QA2(models.Model):
    title = models.CharField(max_length=200)
    qa = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
