from django.shortcuts import render,redirect
from django.contrib import messages
from .import models
from .models import Contact

# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def contact(request):
    print(request.method)
    if request.method == "POST":
        
        # Extracting form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validating form inputs
        if len(name) < 3 or len(name) > 30:
            messages.error(request, 'Name must be between 3 and 30 characters long.')
        elif len(contact) < 3 or len(contact) > 10:
            messages.error(request, 'Contact number must be between 3 and 10 characters long.')
        elif not email or '@' not in email:
            messages.error(request, 'Please enter a valid email address.')
        elif len(subject) < 5:
            messages.error(request, 'Subject must be at least 5 characters long.')
        elif len(message) < 10:
            messages.error(request, 'Message must be at least 10 characters long.')
        else:
            result=models.Contact(name=name,email=email,contact=contact,subject=subject,message=message)
            result.save()
            messages.success(request, 'Your message has been submitted successfully!')
            return redirect('index')
    #return render(request, 'index.html')

