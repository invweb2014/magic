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
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib import messages
from django.template import loader, Context
import json
from django.http import HttpResponse
from magic.security.has_perm import has_perm
from magic.redirect.base import Redirect

from magic.db.list import ListDb
from magic.models import Comment
from django import forms
from magic.form.mform import MForm
from django.template import Context, Template

class CommentForm(MForm):
    parent_template = "magic/index_no_col.html"
    item_ajax_template = "magic/comment_item_ajax.html"    
    model = Comment

    class Meta:
        pass
        model = Comment
        fields = ['name', 'comment']

    def process(self, request):
        self.save_instance()
        self.instance.ref_id = request.GET.get('ref_id')
        self.instance.ref_obj = request.GET.get('ref_obj')
        self.instance.save()
        json = {}
        json_dict = {'substatus':'processed'}
        result = {'json':json_dict, 'comment':self.instance, 'template_rr':self.item_ajax_template}
        return result

    