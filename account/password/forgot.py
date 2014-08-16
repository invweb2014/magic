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


class ForgotPasswordForm(BForm, forms.Form):
    name = "Forgot Password"
    submit_text = "Submit"
    after_title_text = 'Please enter your email below and we will send your instruction to reset your password'
  
    email = forms.EmailField(required=True)
    verify_human = XRechapField();

    def clean_email(self):
        y_email = self.cleaned_data.get('email', '')
        if len(User.objects.filter(email = y_email)) <= 0:
            raise forms.ValidationError("Please enter a valid email")   
        return y_email
 
    def process(self, request):  
        user = User.objects.get(email = self.cleaned_data.get("email", None) )
        
        html = "Click the link below to reset your password"
        Msg.add_msg(request, "Please check your password to recover your password.")
        
        result = {'response':'redirect', 'content':'/a/sign_up'}
        return result