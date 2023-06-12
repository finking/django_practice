from django import forms
import datetime


class ContactForm(forms.Form):
    date_creation = forms.DateField(initial=datetime.date.today(),
                                    help_text='Заполнить форму только в настоящий момент',
                                    label='Дата создания')
    subject = forms.CharField(max_length=100, label='Заголовок')
    message = forms.CharField(max_length=500, label='Сообщение')
    sender = forms.EmailField(label='Email отправителя')
    cc_myself = forms.BooleanField(required=False)  # По-умолчанию required=True, поэтому нужно явно указать False

    # так как форма это класс - поддерживает методы.
    def clean_date_creation(self):
        data = self.cleaned_data['date_creation']
        if data < datetime.date.today():
            raise forms.ValidationError("Дата заполнения раньше, чем сегодняшнее число.")
        elif data > datetime.date.today():
            raise forms.ValidationError("Дата заполнения позже, чем сегодняшнее число.")

        return data
