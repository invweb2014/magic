from magic.node.base import Node
from magic.db.list import ListDb

class List(Node):
    model = None
    template = "magic/list.html"
    parent_template = None
    perm_list = []
    
    page = 1
    item_per_page = 30
    mpp = 100
    sort_by = '-id'
    
    
    @classmethod
    def run(cls, request, get, post, args={}):
        '''argument: cls, request
           return: result dict
        '''
        page = int(request.GET.get('page', cls.page))
        item_per_page = int(request.GET.get('item_per_page', cls.page))
        sort_by = request.GET.get('sort_by', cls.sort_by)
        filters = cls.transform_filter_url_to_dict(request)
        if cls.model:
                e_list = ListDb.get(cls.model, filters, page, item_per_page, sort_by)
                return e_list
        else:
                return {}
