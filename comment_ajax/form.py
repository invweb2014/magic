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
    model = Comment

    parent_template = "magic/index_no_col.html"
    
    class Meta:
        pass
        model = Comment
        fields = ['name', 'comment']

    def process(self, request):
        self.save_instance()
        self.instance.ref_id = request.GET.get('ref_id')
        self.instance.ref_obj = request.GET.get('ref_obj')
        self.instance.save()
        result = {'content':'',  'sub_status':'ajax_complete', 'form':self}
        return result

        
    @classmethod
    def render(cls, request, get, post, args, result):
            if result.get('sub_status') == 'ajax_complete':
                    
                    s = '''
                            <div class="comment">
                                Comment <div class="c">{{c.comment}}</div>
                            </div>
                    '''
                    t = Template(s)
                    c = Context({'c': result['form'].instance})
                    html = t.render(c)
                    json_dict = {'content':html, 'sub_status':'ajax_complete'} #{'item_html':html, 'sub_status':'ajax_complete'},
                    return HttpResponse(json.dumps(json_dict), content_type="application/json")
            result['request'] = request
            result['cls'] = cls
            result['parent_template'] = cls.empty_template
            template_loader = loader.get_template(cls.template)
            context_instance = RequestContext(request)
            context_instance.update(Context(result))
            html = template_loader.render(context_instance)
            
            json_dict = {'content':html}
            return HttpResponse(json.dumps(json_dict), content_type="application/json")
    