from django.db import models


class Payment(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return f"{self.value}"
