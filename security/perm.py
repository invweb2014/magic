class Perm(object):
    @staticmethod
    def check(request, perm_list):
        # check superuser
        if request.user and request.user.is_superuser == True:
            return True
        
        # check thru permission
        pcounter = 0;
        for p in perm_list:
            if p == 'any': 
                pcounter = pcounter + 1
            elif p == 'login_required' and (request.user and request.user.is_authenticated()):
                pcounter = pcounter + 1
            elif request.user.has_perm(p):
                pcounter = pcounter + 1
        # check matching permission      
        if pcounter == len(perm_list):
            return True
        return False