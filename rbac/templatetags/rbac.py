import re

from django.template import Library

register=Library()
@register.inclusion_tag("rbac/menu.html")
def get_menu_style(request):
    permission_menu_list = request.session.get('permission_menu_list')
    for item in permission_menu_list:
        ret = re.search("^{}$".format(item['url']), request.path)
        if ret:
            item['class'] = 'active'
    return {'permission_menu_list':permission_menu_list}