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
    created_by = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='Team Creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()


class TeamMember(models.Model):
    member_id = models.AutoField(primary_key=True, unique=True)
    team_id = models.ForeignKey(Team.team_id, on_delete=models.CASCADE, related_name='Related Team')
    user_id = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='Related Member')
    role = models.CharField(max_length=50, choices=ROLES)
    joined_at = models.DateTimeField(auto_now_add=True)
