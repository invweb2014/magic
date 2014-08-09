from magic.node.base import Node
from magic.db.item import ItemDb
class Item(Node):
	model = None
	template = "magic/item.html"
	parent_template = "magic/index.html"
	perm_list = []
	
	flag_comment = True
	
	@classmethod
	def run(cls, request, get, post, args={}):
		'''argument: cls, request
		   return: result dict
		'''
		id = request.GET.get('id')
		if cls.model and id: 
				instance = ItemDb.get(cls.model, {'id':id})
				return {'e':instance}
		else:
				return {}
