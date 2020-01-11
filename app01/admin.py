from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.User)

class RoleConfig(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(models.Role,RoleConfig)

class PermissionConfig(admin.ModelAdmin):
    list_display = ['pk','title','url','is_menu','icon']
    list_editable = ['title','is_menu']
    search_fields = ['title']
    ordering = ['pk']

admin.site.register(models.Permission,PermissionConfig)