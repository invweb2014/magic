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


class ChangeEmailForm(BForm, forms.Form):
    new_email = forms.CharField(required=True)
    current_password = forms.CharField(widget=forms.PasswordInput, required=True)
  
    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        username = self.request.user.username
        if username and password:
            print "user name is: %s" % username
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Current password is incorrect.")
        return password
 
    def clean_new_email(self):
        new_email = self.cleaned_data.get('new_email', '')
        if len(User.objects.filter(email = new_email)) > 0:
            raise forms.ValidationError("Sorry, the email is already created with another account. ")   
        return new_email
               
    def process(self, request):   
        new_email = self.cleaned_data.get('new_email', '')    
        
        user = request.user
        user.email = new_email
        user.save()
        
        Msg.add_msg(request, "Your email has been change.")
        result = {'response':'redirect', 'content':'/'}
        return result

          

        