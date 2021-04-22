from django.db import models
from django.utils import timezone
from places.fields import PlacesField


class CategoryTags(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


PRIORITY = (
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low'),
)


class ResourcesPost(models.Model):
    link = models.URLField(null=True, blank=True)
    last_update_on = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    location = PlacesField()
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    contacts = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    tags = models.ManyToManyField(CategoryTags)
    


class ResourcesRequest(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=False)
    contact = models.CharField(max_length=256)
    location = PlacesField()
    resolved = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY)
    creation_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(CategoryTags)
