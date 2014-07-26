from settings import MAGIC_NODE

def index(request):
	return Route.route(request, 'index')

class Route(object):
	@staticmethod
	def route(request, node):
		path = MAGIC_NODE[node]['path']
		path = "%s as znode" % path
		
		znode = None
		exec(path)
		
		print "znode: %s" % str(znode)
		result = znode.run(request, request.GET, request.POST, {})
		return znode.render(request, request.GET, request.POST, {}, result)
		
	
			