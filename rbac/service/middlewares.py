import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class PermissionMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        current_path = request.path
        for reg in ['/login/','/admin/']:
            ret=re.search(reg,current_path)
            if ret:
                return None
        user_id=request.session.get('user_id')
        if not user_id:
            return redirect('/login/')


        permission_list=request.session.get('permission_list')
        for reg in permission_list:
            reg='^%s$'%reg
            ret=re.search(reg,current_path)
            if ret:
                return None
        return HttpResponse('无权限访问')