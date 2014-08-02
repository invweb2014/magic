import copy
from magic.node.base import Node
from magic.db.list import ListDb
from magic.db.distinct import DistinctDb

class List(Node):
    
    model = None
    perm_list = []
    
    template = "magic/list.html"
    parent_template = "magic/index.html"
    
    tname = "list"    
    tname_form = "..."
    tsort = ['time_create', 'symbol']
    tfilters = []
    titem_per_page = 30

    @classmethod 
    def get_uparam(cls, request, get, post):
        # normalize
        get = copy.deepcopy(get)
        for k in get.keys():
            v = get[k]
            if "_rr" in k: 
                #get.remove[k]
                get[k.replace("_rr", "")] = v 
        
        for k in get.keys():
            if "_rm" in k:
                k = k.replace("_rm", '')
                del get[k]
        
        # param
        page = int(get.get('page', 1))
        item_per_page = int(get.get('item_per_page', cls.titem_per_page))
        sort_by = get.get('sort', cls.tsort[0])
        filters, filter_list = cls.get_filters(request, get, post)
        url = "/a/%s/?item_per_page=%d&page=%d&sort=%s" % (cls.tname, item_per_page, page, sort_by)
        for k in filters: 
            v = filters[k]
            url = url + "&%s=%s" % (k, v) 
        return page, item_per_page, sort_by, filters, filter_list, url
             
    @classmethod
    def get_filters(cls, request, get, post):
        # get filters in the url
        filters = {}
        for t in cls.tfilters:
            if t in get.keys():
                filters[t] = get[t]
  
        # get the filter list (nav)
        filter_list = {}
        for t in cls.tfilters:
            vals = []
            val_list = DistinctDb.get(cls.model, t)
            for v in val_list: 
                if t in get.keys() and v == get[t]:
                    vals.append({'val':v, 'selected':'yes'})
                else:
                    vals.append({'val':v, 'selected':'no'})
            filter_list[t] =vals
        return filters, filter_list
            
    @classmethod
    def run(cls, request, get, post, args={}):
        '''argument: cls, request
           return: result dict
        '''
        page, item_per_page, sort_by, filters, filter_list,  url_prefix = cls.get_uparam(request, get, post)
        print " =============> filter_list: %s " % str(filter_list)
        if cls.model:
                e_list = ListDb.get(cls.model, filters, page, item_per_page, sort_by)
                e_list['part_tfilters'] = filter_list
                e_list['part_tfilters_selected'] = filters
                part_tpages = [x for x in range(1, e_list['part_paging']['last_page']+1)]
                e_list['part_tpages'] = part_tpages
                e_list['part_tsort'] = cls.tsort
                e_list['part_tsort_selected'] = sort_by
                e_list['url_prefix'] = url_prefix
                return e_list
        else:
                return {'error':'...'}
