from magic.node.base import Node
from magic.db.list import ListDb

class List(Node):
    model = None
    template = "magic/list.html"
    parent_template = "magic/index.html"
    perm_list = []
    
    tsort = ['-id']
    tfilter = []
    titem_per_page = 30
 
    @classmethod 
    def get_ufilters(cls, request, GET, post):
        return {}
   
    
    @classmethod
    def get_tfilters(cls, request, GET, post):
        pass
       
       
    @classmethod
    def run(cls, request, get, post, args={}):
        '''argument: cls, request
           return: result dict
        '''
        page = int(request.GET.get('page', 1))
        item_per_page = int(request.GET.get('item_per_page', cls.titem_per_page))
        sort_by = request.GET.get('sort_by', cls.tsort[0])
        filters = cls.get_ufilters(request, get, post)
        if cls.model:
                e_list = ListDb.get(cls.model, filters, page, item_per_page, sort_by)
                e_list['part_tfilters'] = cls.get_tfilters(request, get, post)
                e_list['part_tfilters_selected'] = filters
        else:
                return {}
