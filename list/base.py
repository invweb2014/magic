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
    def get_filter(cls, request):
        filters = cls.model._meta.get_all_field_names()

    @classmethod
    def transform_filter_url_to_dict(cls, request):
        filters = cls.get_filter(request)
        f = {}
        for k in request.GET.keys():
            if k in filters:
                    f[k] =  request.GET.get(k)
        return f
    
    @classmethod
    def transform_filter_db_to_dict(cls, request):
        filters = cls.model._meta.get_all_field_names()
                    
    @classmethod
    def run(cls, request):
        '''argument: cls, request
           return: result dict
        '''
        page = int(request.GET.get('page', cls.page))
        item_per_page = int(request.GET.get('item_per_page', cls.page))
        sort_by = request.GET.get('sort_by', cls.sort_by)
        filters = cls.transform_filter_url_to_dict(request)
        if cls.model:
                e_list = ListDb.get(cls.model, filters, page, item_per_page, sort_by)
                return {'e_list':e_list}
        else:
                return {}
