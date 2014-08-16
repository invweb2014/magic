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


class LogInForm(BForm, forms.Form):
   
    email = forms.CharField(label="Email", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
        
    tz_html = '''
            <p><a href="/a/forgot_password">Forgout your passowrd?</a></p>
            <p><a href="/a/sign_up">Sign up for new account?</a></p>
    '''
    def clean_email(self):
        email = self.cleaned_data.get('email');
        email_count = ListDb.get(User, {'email':email})['part_paging']['total']
        if email_count != 1: 
            raise forms.ValidationError("Invalid email address")
        return email
                  
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        ulist = ListDb.get(User, {'email':email})['list']
        if len(ulist) == 1: 
            username = ulist[0].username
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Wrong username or password.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")
        return self.cleaned_data

    def process(self, request):  
        auth_login(request, self.user_cache)
        Msg.add_msg(request, "Suceccfully signed in")
        result = {'response':'redirect', 'content':'/'}
        return result
          

        