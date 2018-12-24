from django.db import models
from datetime import datetime
# Create your models here:

class CommentsData(models.Model):
    comments = models.TextField(default="")
    nickname = models.CharField(default="", max_length=20)
    update_date = models.DateTimeField(default=datetime.now, blank=True)
