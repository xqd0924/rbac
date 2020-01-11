from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=11)
    pwd=models.CharField(max_length=11)
    roles=models.ManyToManyField('Role')
    def __str__(self):
        return self.name

class Role(models.Model):
    title=models.CharField(max_length=11)
    permissions=models.ManyToManyField('Permission')
    def __str__(self):
        return self.title

class Permission(models.Model):
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=32)
    is_menu=models.BooleanField(default=False)
    icon=models.CharField(max_length=32,default="")
    def __str__(self):
        return self.title