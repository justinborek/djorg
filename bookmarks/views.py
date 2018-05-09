from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Bookmark

class IndexView(generic.ListView):
    template_name = 'bookmarks/index.html'
    context_object_name = 'bookmark_list'

    def get_queryset(self):
        return Bookmark.objects.order_by('name')
