from uuid import uuid4
from datetime import datetime
from django.db import models


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    url = models.URLField('URL', unique=True)
    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
