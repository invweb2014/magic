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
    tsort = ['id']
    tfilters = []
    titem_per_page = 30
    
    uitem = None

    @classmethod 
    def get_pages(cls, first, last, page, step = 10):
        print "first %d, last: $%d, page: %d, step: %d" % (first, last, page, step) 
        if page == 0: 
            return []
            
        seq = []
        for p in range(page - step, page):
            if(p > 0):
                seq.append(p)
    
        for p in range(page, page + step):
            if(p <= last):
                seq.append(p)
                
        print "seq: %s" % str(seq)
            
        if last > 2: 
            if len(seq) > 0 and seq[0] != 1:
                seq.insert(0, 1)
            if len(seq) > 2  and seq[1] != 2:
                seq.insert(1, 2)
    
        if last > 3: 
            if len(seq) >= 2 and seq[-2] != last - 1:
                seq.append(last - 1 )
            if len(seq) >= 1 and seq[-1] != last:
                seq.append(last)
    
        if len(seq) > 2 and seq[2] != 3:
            seq.insert(2, "...")
        if len(seq) > 2 and seq[-3] != last - 3:
            seq.insert(len(seq)-2, "...")
            
        if len(seq) <= 1:
            return []
        
        return seq
        
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
                e_list['part_tpages'] = cls.get_pages(1, int(e_list['part_paging']['last_page']), int(page))
                e_list['part_tsort'] = cls.tsort
                e_list['part_tsort_selected'] = sort_by
                e_list['url_prefix'] = url_prefix
                return e_list
        else:
                return {'error':'...'}
