import uuid

from django.db import models


class FileMetadata(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=10)
    size = models.PositiveIntegerField()
    location = models.URLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
