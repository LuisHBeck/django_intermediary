from django.shortcuts import render
from django.contrib import messages #add messages to the page context

from .forms import ContacForm


def index(request):
    return render(request, 
                  'index.html'
                )


def contact(request):
    form = ContacForm(request.POST or None)

    if str(request.method) == "POST":
        print(f'POST = {request.POST}')
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print('Sent message:')
            print(f'Name: {name}, E-mail: {email}, Subject: {subject}, Message: {message}')

            messages.success(request, 'E-mail successfully sent')
            form = ContacForm()

        else: 
            messages.error(request, 'Error sending E-mail')
    
    context = {
        'form': form
    }

    return render(request, 
                  'contact.html', 
                  context=context
                )


def product(request):
    return render(request, 
                  'product.html'
                )