from magic.security.perm import Perm
from magic.msg.base import Msg
    
def has_perm(dummy):
    def wrap_outer(f):
            def wrap_inner(*args, **kargs):
                    cls = args[0]
                    request = args[1]
                    print "perm_list: %s " % cls.perm_list
                    flag_perm = Perm.check(request, cls.perm_list)
                    print "flag_perm is: %s" % str(flag_perm)
                    if not flag_perm: 
                        if request.user and request.user.is_authenticated(): 
                            Msg.add_msg(request, 'Oops, you do not have permission to continue.')
                            result = {'response':'redirect', 'content':'/'}
                            return result
                        else:
                            Msg.add_msg(request, "Plese Sign in to continue")
                            result = {'response':'redirect', 'content':'/a/sign_in'}
                            return result
                    else:
                        return f(*args, **kargs)
            return wrap_inner
    return wrap_outer
