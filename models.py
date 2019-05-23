from django.db import models
from django.shortcuts import reverse
class Comment(models.Model):
    body = models.TextField(blank=False, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('chat_url')

    def __str__(self):
        return '{}'.format(self.body)

    class Meta:
        ordering = ['-date_pub']