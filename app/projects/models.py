from django.db import models
import uuid


class Project(models.Model):
    id = models.URLField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    # owner =
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # featured_image =
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
