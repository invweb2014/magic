import math

from magic.db.base import Db
from django.core.paginator import Paginator

class DistinctDb(Db):
    @staticmethod
    def get(model, col):
        result = model.objects.values(col).distinct()
        
        items = []
        for r in result:
            items.append(r[col])
        print "distinct result: %s---->" % str(items)
        return items
        
    