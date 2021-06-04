from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.CharField(max_length=254)

    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    is_anonymous = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
