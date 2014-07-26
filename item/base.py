from magic.node.base import Node

class Item(Node):
	model = None
	template = "magic/item.html"
	parent_template = None
	perm_list = []
	
	@classmethod
	def run(cls, request, get, post, args={}):
		'''argument: cls, request
		   return: result dict
		'''
		id = request.GET.get('id')
		if cls.model and id: 
				instance = None
				return {'e':instance}
		else:
				return {}
