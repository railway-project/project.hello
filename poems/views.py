from django.urls import reverse

from django.contrib import messages
from django.shortcuts import redirect
from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Poem,Comment
from .form import CommentForm
def search(request):
    query = request.GET.get('query', '')
    poems = Poem.objects.filter(content__icontains=query) | Poem.objects.filter(author__icontains=query)
    context = {
        'query': query,
        'results': poems,
        'selected_category': '',  # Set selected category as empty for search results
    }
    return render(request, 'index.html', context=context)

def home(request):
    categories = Poem.objects.values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category')
    query = request.GET.get('query', '')

    if selected_category:
        poems = Poem.objects.filter(category=selected_category)
    else:
        poems = Poem.objects.filter(is_new=True)  # Only fetch new poems for the main page

    context = {
        'poems': poems,
        'selected_category': selected_category,
        'categories': categories,
        'query': query,
    }
    return render(request, 'index.html', context=context)
def poem_detail(request, slug, pk):
    poems = []  # List to store multiple poems
    poems.append(get_object_or_404(Poem, slug=slug, pk=pk))

    context = {
        'poems': poems,
    }
    return render(request, 'rishi_poems.html', context=context)

def post_detail(request, pk, slug):
    poem = get_object_or_404(Poem, pk=pk, slug=slug)
    comments = Comment.objects.filter(poem=poem, active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.poem = poem
            new_comment.save()
            return redirect('poem-detail', pk=pk, slug=slug)
    else:
        comment_form = CommentForm()

    context = {
        'poem': poem,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'post_detail.html', context=context)
def view_system(request, slug, pk):
    poem = get_object_or_404(Poem, pk=pk, slug=slug)
    poem.views += 1
    poem.save()
    context = {
        'poem': poem,
    'views': poem.views
    }
    return render(request, 'rishi_poems.html', context)