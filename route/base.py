from settings import MAGIC_NODE

def index(request):
	return Route.route(request, 'index')

class Route(object):
	@staticmethod
	def route(request, node_name):
		path = MAGIC_NODE[node_name]['path']
		path = "%s as znode" % path
		
		znode = None
		exec(path)
		
		result = znode.run(request, request.GET, request.POST, {})
		return znode.render(request, result)
		
	
			