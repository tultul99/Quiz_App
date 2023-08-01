from django.db import models

# Create your models here.

class quesOne(models.Model):
    ans1 = models.CharField(max_length=10, blank=True, null=True)
    ans2 = models.CharField(max_length=10, blank=True, null=True)
    ans3 = models.CharField(max_length=10, blank=True, null=True)
    ans4 = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.ans1
