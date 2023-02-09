import logging
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

GROUPO_VENDOR = ['vendor']
GRUPO_USUARIO = ['usuario']
MODELS = ['Product']
PERMISSIONS_VENDOR = ['view', 'add', 'change', 'delete']  # For now only view permission by default for all, others include add, delete, change
USER_PERMISSIONS = ['view']

class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        groups = []
        for group_name in GROUPO_VENDOR + GRUPO_USUARIO:
            group, created = Group.objects.get_or_create(name=group_name)
            groups.append(group)

        for group in groups:
            user_permissions = PERMISSIONS_VENDOR if group.name in GROUPO_VENDOR else USER_PERMISSIONS
            permissions = [Permission.objects.get(name='Can {} {}'.format(permission, model))
                           for model in MODELS for permission in user_permissions]

            group.permissions.set(permissions)

        print("Created default group and permissions.")
