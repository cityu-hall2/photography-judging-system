"""
Models for Judges, Entries, Photos
"""

from random import choice
from string import ascii_lowercase

def random_password():
    return ''.join(choice(ascii_lowercase) for i in range(15))

from django.db import models

class Judge(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    year = models.IntegerField()
    password = models.CharField(max_length=20, default=random_password)

    def __str__(self):
        return 'Judge (%d) %s, %s' % (self.year, self.last_name, self.first_name)

class Entry(models.Model):
    judge = models.ForeignKey(
        Judge,
        on_delete=models.CASCADE
        )
    titie = models.CharField(max_length=100)
    internal_identifier = models.CharField(max_length=100, default='-')
    rank = models.IntegerField(default=0)

    def __str__(self):
        rank_str = 'unranked'
        if self.rank > 0:
            rank_str = 'ranked %d' % self.rank
        return '[%s] Entry: %s (%s)' % (rank_str, self.titie, self.internal_identifier)

class Photo(models.Model):
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE
        )
    internal_identifier = models.CharField(max_length=100, default='-')
    order = models.IntegerField(default=0)
    thumbnail_url = models.CharField(max_length=255)
    full_size_url = models.CharField(max_length=255)

    def __str__(self):
        return 'Photo: (%s)' % self.internal_identifier

