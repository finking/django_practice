from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Author
from .forms import AuthorForm


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author_detail'


@login_required
def author_created(request):
    # если запрос Post, только тогда обрабатываем форму.
    if request.method == "POST":

        form = AuthorForm(request.POST)

        if form.is_valid():
            # Не понятно зачем следующие 3 строчки и без них работает
            # Вообще лучше брать как в блоге (blog) или дискуссиях (discussions)

            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            birth_date = form.cleaned_data['birth_date']
    
            new_author = form.save()
            # redirect to a new URL:
            return redirect(new_author.get_absolute_url())
    else:
        form = AuthorForm()

    return render(request, 'model_form/author_form.html', {'form': form})
