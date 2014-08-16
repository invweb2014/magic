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
from django import forms


class ResetPasswordForm(BForm, forms.Form):
    name = "Reset Password"
    submit_text = "Reset Passwaord"
    after_title_text = 'Please enter your email address and password to reset your password'

    email = forms.EmailField(required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password', '')
        if len(password) <= 6: 
            raise forms.ValidationError("Please enter a password that's at least 6 characters long! ") 
        return password
    
    def clean(self):
        if self.cleaned_data.get('new_password', '') != self.cleaned_data.get('confirm_password', ''):
            raise forms.ValidationError("Opps, the new passwords do not match.")            
        return self.cleaned_data  
            
    def process(self, request):              
        user_email  = self.cleaned_data.get("email", None) 
        user = User.objects.get(email=user_email)
        user.set_password(self.cleaned_data.get("new_password", None))

        Msg.add_msg(request, "You password has been updated.")
        result = {'response':'redirect', 'content':'/a/sign_up'}
        return result