import uuid
from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.TextField("Group Name")

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    belonging_group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name="belonging_group", null=True)
    approval_group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name="approval_group", null=True)

    def __str__(self):
        return f"{self.user.username} - {self.belonging_group}"
    

