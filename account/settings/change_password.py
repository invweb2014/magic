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


class ChangePasswordForm(BForm, forms.Form):
    
    current_password = forms.CharField(widget=forms.PasswordInput, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        username = self.request.user.username
        if username and password:
            print "user name is: %s" % username
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Current password is incorrect.")
        return password
            
    def clean_new_password(self):
        y_password = self.cleaned_data.get('new_password', '')
        if len(y_password) <= 6: 
            raise forms.ValidationError("Please enter a password that's at least 6 characters long! ") 
        return y_password

    def clean(self):
        if self.cleaned_data.get('new_password', '') != self.cleaned_data.get('confirm_password', ''):
            raise forms.ValidationError("Opps, the new passwords do not match.")            
        return self.cleaned_data  
            
    def process(self, request):       
        user = request.user
        user.set_password(self.cleaned_data.get("new_password", None))
        user.save()

        Msg.add_msg(request, "Your password has been change.")
        result = {'response':'redirect', 'content':'/'}
        return result

          

        