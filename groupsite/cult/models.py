from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    liked_me = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.title} like {self.liked_me}"


class User(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)  #TODO: use authentication
    i_liked = models.PositiveSmallIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.name} gave {self.i_liked}"
