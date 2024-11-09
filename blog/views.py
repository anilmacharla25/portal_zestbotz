from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from blog.models import Contact
from .forms import ContactForm, ResumeSubmissionForm
import yagmail

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            #messages.success(request, 'Your message has been sent!')
            return redirect('home')
        else:
            pass
            # messages.error(request, 'Name and message fields cannot be empty.')

    return render(request, 'home.html')


def submit_resume(request):
    if request.method == 'POST':
        form = ResumeSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            resume = request.FILES['resume']

            try:
                
                yag = yagmail.SMTP(settings.EMAIL_HOST_USER)

                
                subject = f'New Resume Submission from {name}'
                body = f'You have received a new resume submission from {name} ({email}).'

                yag.send(
                    to='anishagazi29@gmail.com',  
                    subject=subject,
                    contents=body,
                    attachments=resume.file  
                )

                messages.success(request, 'Your resume has been submitted and emailed successfully!')
                return redirect('home')

            except Exception as e:
                
                messages.error(request, f'Failed to send the resume via email. Error: {str(e)}')
        else:
            messages.error(request, 'There was an error submitting your resume. Please try again.')
    else:
        form = ResumeSubmissionForm()
    
    return render(request, 'home.html', {'form': form})

def healthcare_page(request):
    return render(request, 'healthcare.html')

def finance_page(request):
    return render(request, 'finance.html')

def insurance_page(request):
    return render(request, 'insurance.html')
