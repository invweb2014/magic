from django.http import HttpResponseRedirect

class Redirect(object):
    @staticmethod
    def redirect(request, url):
         return HttpResponseRedirect(url)
    