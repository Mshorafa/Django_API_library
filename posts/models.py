from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    """Model definition for Posts."""

    title = models.CharField(max_length=50)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Posts."""
        ordering = ['created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Posts."""
        return self.title


class Votes(models.Model):
    """Model definition for votes."""

    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)


    class Meta:
        """Meta definition for votes."""

        verbose_name = 'votes'
        verbose_name_plural = 'votess'

    def __str__(self):
        """Unicode representation of votes."""
        return f'{self.voter}'
