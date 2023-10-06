from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Employee

@receiver(post_save, sender=User)
def create_user_picks(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
        instance.groups.add(Group.objects.get(name='Employee'))