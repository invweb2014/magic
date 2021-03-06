import math

from magic.db.base import Db
from django.core.paginator import Paginator

class ListDb(Db):
    @staticmethod
    def get(model, filters, page = 1, item_per_page = 30, sort_by = None):
        page = int(page)
        print "****************************page: %d" % page
        filter_str = ''
        if len(filters.keys()) > 0:
            for k in filters.keys():
                filter_str = filter_str + ".filter(%s='%s')" % (k, filters[k])
        
        #build order by
        if sort_by: 
            filter_str = filter_str + ".order_by('%s')" %  sort_by            
        
        # run the query
        instant_list = None
        db_str = "instant_list = model.objects.all()%s" % filter_str
        print "************************db_str: %s" % db_str
        exec(db_str)
        
        # paging
        paginator = Paginator(instant_list, item_per_page) 
        result = paginator.page(page).object_list;
        total = paginator.count
        
        start = 1 + item_per_page * (page - 1)
        end =  start + len(result) - 1   
        last_page =  int(math.ceil(float(total)/item_per_page))
        
        return {    'list':result,
                    'part_paging':{'page':page,
                                'start':start,
                                'end':end,
                                'total':total,
                                'last_page':last_page
                               },
                }
        
    