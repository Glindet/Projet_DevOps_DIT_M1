from django.db import models

# Create your models here.
class Task(models.Model):
    content = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content