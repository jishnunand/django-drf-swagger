from django.db import models


class Tags(models.Model):
    """
    Table which holds Tags for Assessment
    """
    name = models.CharField(max_length=50)


class Assessment(models.Model):
    """
    Table which will hold Assessment data
    """
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    tags = models.ManyToManyField(Tags)
