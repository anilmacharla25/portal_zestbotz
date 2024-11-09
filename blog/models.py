from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    
class ResumeSubmission(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name