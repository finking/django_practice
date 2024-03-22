from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/index.html",context )


class UserPostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/user_posts.html'

    context_object_name = 'blog_post_user_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')

    # def get_context_data(self, **kwargs):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     queryset = Post.objects.filter(author=user)
    #     context = super().get_context_data(**kwargs)
    #     context['blog_post_user_list'] = queryset.order_by('-date_created')
    #     return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.pk})


# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'blog_post_detail'
def PostDetailView(request, pk):
    handle_page = get_object_or_404(Post, id=pk)
    total_comments = handle_page.comments_blog.all().filter(reply=None).order_by('-id')
    total_comments_all = handle_page.comments_blog.all().order_by('-id')
    total_likes = handle_page.total_likes_post()
    total_saves = handle_page.total_saves_posts()

    context = {}
    
    context["blog_post_detail"] = handle_page
    
    return render(request, 'blog/post_detail.html', context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('user-posts-list', args=[self.request.user])
   
    template_name = 'blog/post_delete.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()  # UpdateView → BaseUpdateView → ModelFormMixin → SingleObjectMixin
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.pk})