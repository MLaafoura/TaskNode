from django.db import models
from taskNodeUser.models import CustomUser
from taskNodeTeams.models import Team


class Project(models.Model):
    project_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='projects', null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
