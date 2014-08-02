from django.contrib import messages

class Msg(object):
    @staticmethod
    def add_msg(request, msg):
        messages.add_message(request, messages.INFO, msg)
    
    @staticmethod
    def retrieve_msg(request, url):
        pass