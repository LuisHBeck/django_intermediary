from django import forms 
from django.core.mail.message import EmailMessage

from .models import Product

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=25)
    email = forms.EmailField(label='E-mail', max_length=50)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea())
    
    
    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        
        content = f'Name: {name}, E-mail: {email}, Subject: {subject}, Message: {message}'
        
        mail = EmailMessage(
            subject='E-mail sent by Django system',
            body=content,
            from_email='contact@djangoproject.com.br',
            to=['contact@djangoproject.com.br'],
            headers={'Reply-To': email}
        )
        
        mail.send()
        
        
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','stock', 'image']