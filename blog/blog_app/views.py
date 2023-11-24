from django.shortcuts import render
from blog_app.models import Post
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)


def about(request):
    """View function for about page of site.
    
        param request: request object
        return: HttpResponse object
    """
    return render(request, 'blog_app/about.html', {'title': 'About'})

class PostListView(ListView):
    """Generic class-based view for a list of posts.
    
    Attributes:
        model: model for PostListView
        template_name: template for PostListView
        context_object_name: context for PostListView
        ordering: ordering for PostListView
    """
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostCreateView(LoginRequiredMixin, CreateView):
    """Generic class-based view for creating a post.
    
    Attributes:
        model: model for PostCreateView
        fields: fields for PostCreateView
    """
    model = Post
    fields = ['title', 'content']
    success_url = '/'
    
    def form_valid(self, form):
        """Method to validate form.
        
        param form: form to validate
        return: super().form_valid(form)
        """
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    """Generic class-based view for a detail view of a post.
    
    Attributes:
        model: model for PostDetailView
    """
    model = Post
    context_object_name = 'post'

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """Generic class-based view for updating a post.
    
    Attributes:
        model: model for PostUpdateView
        fields: fields for PostUpdateView
    """
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_app/post_update.html'

    def form_valid(self, form):
        """Method to validate form.

        param form: form to validate
        """
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """Method to test if user is author of post.
        
        Returns:
            True if user is author of post, False otherwise
        """
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """Generic class-based view for deleting a post.
    
    Attributes:
        model: model for PostDeleteView
        success_url: success_url for PostDeleteView
    """
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = '/'
    
    def test_func(self):
        """Method to test if user is author of post.
        
        Returns:
            True if user is author of post, False otherwise
        """
        post = self.get_object()
        return self.request.user == post.author