from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Configura grupos y usuarios iniciales'

    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='administradores')
        user_group, created = Group.objects.get_or_create(name='usuarios')

        admin_user, created = User.objects.get_or_create(username='admin')
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
        admin_user.groups.add(admin_group)

        basic_user, created = User.objects.get_or_create(username='usuario')
        if created:
            basic_user.set_password('usuario123')
            basic_user.save()
        basic_user.groups.add(user_group)

        self.stdout.write(self.style.SUCCESS('Grupos y usuarios creados exitosamente.'))
