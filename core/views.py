from django.shortcuts import render
from django.contrib import messages #add messages to the page context

from .forms import ContactForm, ProductModelForm


def index(request):
    return render(request, 
                  'index.html'
                )


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == "POST":
        # print(f'POST = {request.POST}')
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']

            # print('Sent message:')
            # print(f'Name: {name}, E-mail: {email}, Subject: {subject}, Message: {message}')
            
            form.send_mail()

            messages.success(request, 'E-mail successfully sent')
            form = ContactForm()

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
    
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        
        if form.is_valid():
            prod = form.save(commit=False)
            
            print(f'Name:{prod.name}, Price:{prod.price}, Stock:{prod.stock}, Image:{prod.image}')
            
            messages.success(request, "Saved successfully")
            form = ProductModelForm()
            
        else:
            messages.error(request, "ERROR saving")
            form = ProductModelForm()
    else:
        form = ProductModelForm()
        
    context = {
        'form':form
    }
    
    return render(request, 
                  'product.html',
                  context=context,
                )