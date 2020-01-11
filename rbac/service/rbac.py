from app01.models import Role

def initial_session(user,request):
    permissions = Role.objects.filter(user=user).values('permissions__url',
                                                        'permissions__is_menu',
                                                        'permissions__icon',
                                                        'permissions__title'
                                                        ).distinct()
    permission_list = []
    permission_menu_list = []
    for item in permissions:
        permission_list.append(item['permissions__url'])
        if item['permissions__is_menu']:
            permission_menu_list.append({
                'title':item['permissions__title'],
                'icon':item['permissions__icon'],
                'url':item['permissions__url']
            })
    request.session['permission_list'] = permission_list
    request.session['permission_menu_list'] = permission_menu_list
    print('menu',permission_menu_list)