from django.db import models

class Todo(models.Model):
    """A Todo Model"""
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        """return title for todo"""
        return self.body
