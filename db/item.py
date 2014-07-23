from magic.db.base import Db

class ItemDb(Db):
    @staticmethod
    def get(model, filters={}):
        e = None
        db_str = "e = models.objects.get(id=%s)" % filters['id']
        exec(db_str)
        return e
    
    @staticmethod
    def save(model, filters={}):
        e = model()
        if len(filter.keys()) > 0:
            for k in filter.keys():
                exec("%s_val = filters[k]" % k)
                exec("e.%s = %s_val" % (k, k))
        e.save()
        return e
    
    @staticmethod
    def delete(model, filters):
        e = ItemDb.get(model, filters)
        e.delete()   