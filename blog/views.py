from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/post_confirm_delete.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
