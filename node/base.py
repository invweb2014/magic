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

class Node(object):
    model = None
    template = "magic/index.html"
    empty_template = "magic/empty.html"
    parent_template = None
     
    perm_list = []

    @classmethod
    @has_perm(['dummy',])
    def run(cls, request, get, post, args={}):
        '''argument: cls, request
           return: result dict
        '''
        return {}
    
    @classmethod
    def render(cls, request, get, post, args, result):
        result['cls'] = cls
        result['request'] = request
        
        # get response type
        if request.is_ajax():
            response = "ajax"
        else:
            response = "html"
            
        print "**********************************************is ajax: %s" % str(request.is_ajax())
        print "**********************************************response: %s" % str(response)
        
        if response == 'html':
            result['parent_template'] = cls.parent_template
            return render_to_response(cls.template, result, context_instance=RequestContext(request),)
        elif response == 'ajax':
            result['parent_template'] = cls.empty_template
            template_loader = loader.get_template(cls.template)
            context_instance = RequestContext(request)
            context_instance.update(Context(result))
            html = template_loader.render(context_instance)  
            result = {}
            result['content'] = html
            return HttpResponse(json.dumps(result), content_type="application/json")
        elif response == 'redirect':
            return Redirect.redirect(request, result['content'])
    
           
        
        
        