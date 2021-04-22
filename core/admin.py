from django.contrib import admin

from .models import CategoryTags, ResourcesPost, ResourcesRequest

admin.site.register(CategoryTags)
admin.site.register(ResourcesPost)
admin.site.register(ResourcesRequest)