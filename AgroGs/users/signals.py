from django.contrib.auth.models import Group
from .models import User, UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance).save()
        if instance.is_staff:
            groups = Group.objects.filter(name='vendor')
            if groups:
                for group in groups:
                    instance.groups.add(group.id)
        
        