from django.db import models

class TestModel(models.Model):
    fieldself = models.CharField(
        max_length=300,
        verbose_name="Insert Text Here"
        )
    fieldsignal = models.CharField(
        null = True,
        blank = True,
        max_length=300,
        verbose_name="Do not touch it"
        )
    def __str__(self):
        return self.fieldself
