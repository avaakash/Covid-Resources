from django.shortcuts import render, redirect

from .models import ResourcesPost, ResourcesRequest
from .forms import AddResourceInformation, AddResourceRequest


def home(request):
    resources_information = ResourcesPost.objects.filter(
        available=True).order_by('last_update_on')
    resources_request = ResourcesRequest.objects.filter(
        resolved=False).order_by('priority', 'creation_time')
    context = {
        'resources': resources_information,
        'requests': resources_request
    }
    return render(request, 'home.html', context)

def add_resource(request):
    form = AddResourceInformation(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_resources.html', {'form': form})

def request_resource(request):
    form = AddResourceRequest(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_requests.html', {'form': form})
