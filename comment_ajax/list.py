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
    template = 'magic/list_ajax.html'
    
    @classmethod
    def render(cls, request, get, post, args, result):
            result['request'] = request
            result['cls'] = cls
            result['parent_template'] = cls.empty_template
            template_loader = loader.get_template(cls.template)
            context_instance = RequestContext(request)
            context_instance.update(Context(result))
            html = template_loader.render(context_instance)
            
            json_dict = {'content':html, 'part_paging':result['part_paging']}
            return HttpResponse(json.dumps(json_dict), content_type="application/json")
    
        