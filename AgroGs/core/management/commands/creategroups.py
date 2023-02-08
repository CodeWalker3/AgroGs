"""
Create permission groups
Create permissions (read only) to models for a set of groups
"""
import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

GROUPO_VENDOR = ['vendor']
GRUPO_USUARIO = ['usuario']
MODELS = ['Product']
PERMISSIONS_VENDOR = ['view', 'add', 'change', 'delete']  # For now only view permission by default for all, others include add, delete, change
USER_PERMISSIONS = ['view']

class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        for group in GROUPO_VENDOR:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                for permission in PERMISSIONS_VENDOR:
                    name = 'Can {} {}'.format(permission, model)
                    print("Creating {}".format(name))

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue

                    new_group.permissions.add(model_add_perm)
        for group in GRUPO_USUARIO:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELS:
                for permission in USER_PERMISSIONS:
                    name = 'Can {} {}'.format(permission, model)
                    print("Creating {}".format(name))

                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue

                    new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")