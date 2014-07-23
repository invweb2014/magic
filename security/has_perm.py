from magic.security.perm import Perm

def has_perm(dummy):
    def wrap_outer(f):
            def wrap_inner(*args, **kargs):
                    cls = args[0]
                    request = args[1]
                    flag_perm = Perm.check(request, cls.perm_list)
                    print "flag_perm is: %s" % str(flag_perm)
                    if not flag_perm: 
                        if request.user and request.user.is_authenticated(): 
                            message = 'Oops, you do not have permission to continue.'
                        else:
                            message = 'Please sign in to continue.'
                        print "need to redirect to somewhere"
                    return f(*args, **kargs)
            return wrap_inner
    return wrap_outer
