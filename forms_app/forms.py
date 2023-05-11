from django import forms
import datetime


class ContactForm(forms.Form):
    date_creation = forms.DateField(initial=datetime.date.today(), help_text='Заполнить форму только в настоящий момент')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)  # По-умолчанию required=True, поэтому нужно явно указать False

    # так как форма это класс - поддерживает методы.
    def clean_date_creation(self):
        date = self.cleaned_data['date_creation']
        if date < datetime.date.today():
            raise forms.ValidationError("Дата заполнения раньше, чем сегодняшнее число.")
