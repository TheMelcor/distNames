from django import forms


class NameForm(forms.Form):
    submit_name = forms.CharField(label='Your Name', max_length=50)
