from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Thread, Post
from .forms import ThreadForm, PostForm
from django.http import HttpResponse

# List all threads
class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'
    context_object_name = 'object_list'

# View a single thread and its posts
class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

# Create a new thread
class CreateThreadView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/create_thread.html'
    success_url = reverse_lazy('forum:thread-list')

# Create a new post in a thread
def create_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.author = request.user  # Make sure user is logged in
            post.save()
            return redirect('forum:thread-detail', pk=thread.id)
        # If form is invalid, we'll show errors below
    else:
        form = PostForm()  # GET: show empty form

    return render(request, 'forum/create_post.html', {
        'form': form,
        'thread': thread
    })