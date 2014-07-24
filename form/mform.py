from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib import messages
from django.template import loader, Context
from django.forms import ModelForm
from magic.security.has_perm import has_perm
from magic.node.base import Node
from magic.db.item import ItemDb
from magic.form.base import BForm
'''
    MEDIA_URL = '/xapp-htdocs/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'deals_htdocs')
    
    image_file = models.FileField(upload_to='deals_upload')
    
    image_path = os.path.join(settings_prod.MEDIA_ROOT, str(self.instance.image_file))
    ImageResize.image_resize(image_path, image_path, 200, 300)    
'''

class MForm(ModelForm, BForm):
    model = None
    template = "magic/ftable.html"
    parent_template = None
    perm_list = []
    need_ownership = False
 
    class Meta:
        pass
        model = None