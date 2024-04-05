from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post, Comment
from .forms import CommentForm
import random


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
def post_detail_view(request, pk):
    handle_page = get_object_or_404(Post, id=pk)
    total_comments = handle_page.comments_blog.all().filter(reply=None).order_by('-id')
    total_comments_all = handle_page.comments_blog.all().order_by('-id')
    total_likes = handle_page.total_likes_post()
    total_saves = handle_page.total_saves_posts()

    context = {}
    
    if request.method == "POST":
        comments_qs = None
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            form = request.POST.get("body")

            comment = Comment.objects.create(post=handle_page,
                                             name_author=request.user,
                                             body=form,
                                             reply=comments_qs)
            comment.save()
            total_comments = handle_page.comments_blog.filter(reply=None).order_by('-id')
    else:
        comment_form = CommentForm()
        
    saved = False
    
    if handle_page.saves_posts.filter(id=request.user.id).exists():
        saved = True
    
    context["saves_posts"] = total_saves
    context["saved"] = saved
    
    context["blog_post_detail"] = handle_page
    # context["comment_form"] = comment_form
    context["comments"] = total_comments

    if request.is_ajax():
        html = render_to_string('blog/comments.html', context)
        return JsonResponse({"form": html})
    
    return render(request, 'blog/post_detail.html', context)


@login_required()
def save_post_is_ajax(request):
    
    post = get_object_or_404(Post, id=request.POST.get('id'))
    saved = False
    
    if post.saves_posts.filter(id=request.user.id).exists():
        post.saves_posts.remove(request.user)
    else:
        post.saves_posts.add(request.user)
        saved = True
    
    total_saves = post.total_saves_posts()
        
    context = {
        'blog_post_detail': post,
        'saved': saved,
        'total_saves': total_saves,
    }
    
    if request.is_ajax():
        html = render_to_string('blog/save_section.html',
                                context,
                                request=request)
        
        return JsonResponse({'form': html})


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
    
    
class HomePostListViewAllUsers(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_created']
    paginate_by = 3
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePostListViewAllUsers, self).get_context_data()
        users = list(User.objects.exclude(pk=self.request.user.pk))

        if len(users) > 3:
            out = 3
        else:
            out = len(users)
            
        random_users = random.sample(users, out)
        context['random_users'] = random_users
        
        return context


# Save posts
@login_required()
def all_save_view_posts(request):
    user = request.user
    saved_posts = user.saves_posts.all()
    context = {'saved_posts': saved_posts}
    
    return render(request, 'blog/saved_posts.html', context)
