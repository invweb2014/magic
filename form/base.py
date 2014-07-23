from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib import messages
from django.template import loader, Context
from magic.security.has_perm import has_perm

from magic.node.base import Node

'''
    MEDIA_URL = '/xapp-htdocs/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'deals_htdocs')
    
    image_file = models.FileField(upload_to='deals_upload')
    
    image_path = os.path.join(settings_prod.MEDIA_ROOT, str(self.instance.image_file))
    ImageResize.image_resize(image_path, image_path, 200, 300)    
'''

class MForm(Node):
    model = None
    template = "magic/ftable.html"
    parent_template = None
    perm_list = []
    
    need_ownership = False
    
    @classmethod
    @has_perm(['dummy',])
    def run(cls, request):
        '''argument: cls, request
           return: result dict
        '''
        def instantiate_form(cls, request):
            pass
  
        result = {}
        if request.method == 'GET': 
            form = instantiate_form(cls, request) 
            if form.is_valid(): 
                result =  form.process(request)
        elif request.method == 'POST': 
            form = instantiate_form(cls, request)
        return {'form':form, 'result':result}
    
    @classmethod
    def render(cls, request, result):
        '''argument: cls, request
           return: result string
           desc: doing the REDIRECT, AJAX, HTML RETURN HERE!!!
        '''
        return render_to_response(cls.template, result, context_instance=RequestContext(request),)
            
    @staticmethod
    def render_ajax(cls, request, result):
        '''argument: cls, request
           return: result json
        '''
        pass
    
    #@post_after
    def process(self, request):
        self.save()
        return cls.render(request, result)
        