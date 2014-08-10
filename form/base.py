from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib import messages
from django.template import loader, Context
from django.forms import ModelForm

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
from django.template import Context, Template

from magic.security.has_perm import has_perm
from magic.node.base import Node
from magic.db.item import ItemDb

'''
    MEDIA_URL = '/xapp-htdocs/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'deals_htdocs')
    
    image_file = models.FileField(upload_to='deals_upload')
    
    image_path = os.path.join(settings_prod.MEDIA_ROOT, str(self.instance.image_file))
    ImageResize.image_resize(image_path, image_path, 200, 300)    
'''

class BForm(Node):
    model = None
    template = "magic/ftable.html"
    parent_template = "magic/index.html"
    ajax_template = "magic/ftable.html"
    
    perm_list = []
    fownership = False
    fupload = False
      
    tname = "My Form"
    tsubmit = "Submit"
    tclass = "my-form"
    
    @classmethod
    @has_perm(['dummy',])
    def run(cls, request, get, post, args={}):
        '''argument: cls, request
           return: result dict
        '''
        if request.method == 'GET': 
            if cls.model and request.GET.get('id'):
                e = ItemDb.get(cls.model, {'id':request.GET.get('id')});
                form = cls(instance=e)
            else:
                form = cls()
            return {'form':form, 'response':'html'}
        elif request.method == 'POST':
            if cls.model and request.GET.get('id'):
                e = ItemDb.get(cls.model, {'id':request.GET.get('id')});
                form = cls(request.POST, request.FILES, instance=e)
            else:
                form = cls(request.POST)
            if form.is_valid(): 
                return form.process(request)
            return {'form':form}

    def process(self, request):
        self.save()
        result = {'response':'redirect', 'content':'/', 'substatus':'processed'}
        return result
    
        