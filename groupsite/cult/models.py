from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    received_likes = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.title} has {self.received_likes} like(s)"


class User(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)  #TODO: use authentication
    posted_likes = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.name} gave {self.posted_likes} like(s)"
