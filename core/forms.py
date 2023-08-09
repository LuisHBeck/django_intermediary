from django import forms 

class ContacForm(forms.Form):
    name = forms.CharField(label='Name', max_length=25)
    email = forms.EmailField(label='E-mail', max_length=50)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea())