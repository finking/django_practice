from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Discussion
from .forms import DiscussionCreateForm


class UserDiscussionListView(ListView):
    model = Discussion
    template_name = 'discussions/user_discussion.html'

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['blog_discussion_list'] = queryset.order_by('-date_created')
        return context


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = Discussion
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DiscussionDetailView(DetailView):
    model = Discussion
    context_object_name = 'discussion_detail'


@login_required
def discussion_created(request):
    # если запрос Post, только тогда обрабатываем форму.
    if request.method == "POST":

        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()
            messages.success(request, "Дискуссия успешно добавлена!")
            return redirect(new_discussion.get_absolute_url())
    else:
        form = DiscussionCreateForm()

    return render(request, 'discussions/discussion_form.html', {'form': form})
