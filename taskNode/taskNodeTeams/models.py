from django.db import models
from taskNodeUser.models import CustomUser


ROLES = [
        ('MEMBER', 'Member'),
        ('ADMIN', 'Admin'),
        ('OWNER', 'Owner')
]


class Team(models.Model):
    team_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='team_creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()


class TeamMember(models.Model):
    member_id = models.AutoField(primary_key=True, unique=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_members')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='related_member')
    role = models.CharField(max_length=50, choices=ROLES)
    joined_at = models.DateTimeField(auto_now_add=True)
