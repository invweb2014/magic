from magic.item.base import Item
from django.contrib.auth import logout
from magic.msg.base import Msg

class Logout(Item):
    @classmethod
    def run(cls, request, get, post, args={}):
        '''argument: cls, request
           return: result dict
        '''
        logout(request)
        Msg.add_msg(request, "You have been logged out")
        result = {'response':'redirect', 'content':'/'}
        return result