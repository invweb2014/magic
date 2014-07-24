from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib import messages
from django.template import loader, Context
from magic.security.has_perm import has_perm

class Node(object):
    model = None
    template = "magic/index.html"
    parent_template = None
    perm_list = []

    @classmethod
    @has_perm(['dummy',])
    def run(cls, request):
        '''argument: cls, request
           return: result dict
        '''
        return {}
    
    @classmethod
    def render(cls, request, result):
        '''argument: result{'response':'html|ajax|redirect'}
                     json: return {'response_type':'confirm|redirect|error|html', 'content':'...'}
           return: ( html | json | redirect )
        '''
        if result['response_type'] == 'html':
            return render_to_response(cls.template, result, context_instance=RequestContext(request),)
        elif result['response'] == 'ajax':
             pass
        elif result['redirect'] == 'html': 
            pass
           
        
        
        