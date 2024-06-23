from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import Empresa, Videojuego

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='administradores')
        user_group, created = Group.objects.get_or_create(name='usuarios')
        
        empresa_ct = ContentType.objects.get_for_model(Empresa)
        videojuego_ct = ContentType.objects.get_for_model(Videojuego)
        
        permissions = Permission.objects.filter(content_type__in=[empresa_ct, videojuego_ct])
        admin_group.permissions.set(permissions)
        
        view_permissions = permissions.filter(codename__startswith='view')
        add_permissions = permissions.filter(codename__startswith='add')
        change_permissions = permissions.filter(codename__startswith='change')
        
        user_group.permissions.set(view_permissions | add_permissions | change_permissions)
        
        self.stdout.write(self.style.SUCCESS('Grupos y permisos creados exitosamente.'))
