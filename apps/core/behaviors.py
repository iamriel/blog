import uuid

from django.db import models


class UUIDable(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )

    class Meta:
        abstract = True


class Timestampable(models.Model):
    creation_date = models.DateTimeField("date created", auto_now_add=True)
    modified_date = models.DateTimeField("date last modified", auto_now=True)

    class Meta:
        abstract = True
