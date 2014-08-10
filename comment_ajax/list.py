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

from magic.list.base import List
from magic.models import Comment

class CommentList(List):
    model = Comment
    ajax_template = 'magic/list_ajax.html'
    

    
        