from django import forms
from .models import ResumeSubmission
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class ResumeSubmissionForm(forms.ModelForm):
    class Meta:
        model = ResumeSubmission
        fields = ['name', 'email', 'resume']