from magic.form.base import BForm
from magic.msg.base import Msg
from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib import messages

from magic.db.list import ListDb
from magic.recaptchat.base import XRechapField
from django import forms


class SignUpForm(BForm, forms.Form):
    email = forms.EmailField(required=True, help_text="We never share your email address with anyone!")
    display_name = forms.CharField(required=True, help_text="This will be your public username on the site.")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Please enter a password that's at least 6 characters long.")
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Please type your password again.")
    verify_human = XRechapField();

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if len(User.objects.filter(email = email)) > 0:
            raise forms.ValidationError("Sorry, the email is already created with another account. ")   
        return email
  
    def clean_display_name(self):
        display_name = self.cleaned_data.get('display_name', '')
        if len(display_name) <= 6: 
            raise forms.ValidationError("Please enter a display name that's at least 6 characters long! ") 
        if len(User.objects.filter(username = display_name)) > 0:
            raise forms.ValidationError("Sorry, this name has been used by someone already! Please try something else. ") 
        return display_name
         
    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) <= 6: 
            raise forms.ValidationError("Please enter a password that's at least 6 characters long! ") 
        return password
    
    def clean(self):
        if self.cleaned_data.get('password', '') != self.cleaned_data.get('confirm_password', ''):
            raise forms.ValidationError("Opps, passwords do not match.")            
        return self.cleaned_data  

    def process(self, request): 
        # Create user account                
        user_email  = self.cleaned_data.get("email", None) 
        username    = self.cleaned_data.get("display_name", None)
        password    = self.cleaned_data.get("password", None)
        
        new_user = User.objects.create_user(username, user_email, password=password)
        new_user.is_active = True
        new_user.save()
        
        Msg.add_msg(request, "Thank you, your account has been created!")
        result = {'response':'redirect', 'content':'/'}
        return result
        
    

        