from django.db import models

# Create your models here.
class ToDo(models.Model):
    added_date=models.DateTimeField()
    text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural="texts"

    def __str__(self):
        return self.text
