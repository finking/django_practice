from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_send(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            date_creation = form.cleaned_data['date_creation']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['finking@yandex.ru']
            if cc_myself:
                recipients.append(message)

            try:
                send_mail(subject, message, sender, recipients)

            except BadHeaderError:
                return HttpResponse("Неверное заполнение")

            form = ContactForm()
            messages.success(request, "Сообщение успешно отправлено.")

        else:
            messages.error(request, "Форма не отправлена. Исправьте ошибки ниже.")

    else:
        form = ContactForm()

    return render(request, 'forms_app/email.html', {"form": form})

