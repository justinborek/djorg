from django.shortcuts import render

from .forms import BookmarkForm
from .models import Bookmark

def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
          form.save()  
    context = {}
    context['bookmarks'] = Bookmark.objects.all()
    context['form'] = BookmarkForm()
    return render(request, 'bookmarks/index.html', context)
