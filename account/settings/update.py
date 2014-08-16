class AccountNode(SingleNode):
    model = None
    name_list = ""
    name_single = ""
    name_form = ""
    template_parent = "lonely_point/index.html"
    template = "xapp/account.html"

    @classmethod
    def view(cls, request, args=None):
        instance = None
        data = None
        return_dict = {'instance':instance, 'node_cls':cls, 'data':data}
        html = RenderHelper.render(cls.template, cls.template_parent, return_dict, request)              
        return {'header':'html', 'content':html} 