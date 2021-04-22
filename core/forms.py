from django import forms

from .models import ResourcesPost, ResourcesRequest


class AddResourceInformation(forms.ModelForm):
    class Meta:
        model = ResourcesPost
        fields = ['title', 'link', 'location',
                  'last_update_on', 'description', 'contacts']


class AddResourceRequest(forms.ModelForm):
    class Meta:
        model = ResourcesRequest
        fields = ['title', 'contact',
                  'location', 'description']
