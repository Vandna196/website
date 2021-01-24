from django import forms 
from .models import *
class Form(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'contact-input white-input',
        'placeholder':'Full Name*',
        'name':'contact_names',
        
        }))
    email_address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'contact-input white-input',
        'placeholder':'Email Address*',
        'name':'contact_email',
        
        }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class':'contact-input white-input',
        'placeholder':'Phone Number*',
        'name':'contact_phone',
        
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20 ,'placeholder':'Your Message...'}))
    class Meta():
        model = Message_form
        fields = ['full_name','email_address','phone_number','message']

class Newform(forms.Form):
    email_address = forms.CharField(widget=forms.TextInput(attrs={
        'id':'email_newsletter',
        'placeholder':'Enter Your Email Address',
        'name':'nf_email',
        
        }))