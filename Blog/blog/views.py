from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm, PostForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

def Profile(request):
    return render(request, 'profile.html')

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']