from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm
from django.core.mail import EmailMessage


def index(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            template = get_template('contact_form.txt')
            context = {
                'name': name,
                'email': email,
                'message': message,
            }

            content = template.render(context)

            email = EmailMessage(
                "Contact Email",
                content,
                "Kinder Mail" + '',
                ['sabint017@gmail.com'], ['sajanmahat491@gmail.com'],
                headers={'Reply To': email}
            )

            email.send()

            return render(request, 'succ.html')
    return render(request, 'index.html', {'form': Contact_Form})


def queries(request):
    return render(request, 'queries.html')


def dev(request):
    return render(request, 'dev.html')


def services(request):
    return render(request, 'services.html')


def signup(request):
    return render(request, 'signup.html')


def contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            template = get_template('contact_form.txt')
            context = {
                'name': name,
                'email': email,
                'message': message,
            }

            content = template.render(context)

            email = EmailMessage(
                "Contact Email",
                content,
                "Kinder Mail" + '',
                ['sabint017@gmail.com'], ['sajanmahat491@gmail.com'],
                headers={'Reply To': email}
            )

            email.send()

            return render(request, 'succ.html')
    return render(request, 'contact.html', {'form': Contact_Form})
# Create your views here.
