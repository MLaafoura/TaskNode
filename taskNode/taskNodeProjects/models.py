from django.db import models
from taskNodeUser.models import CustomUser
from taskNodeTeams.models import Team


class Project(models.Model):
    project_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    team_id = models.ForeignKey(Team.team_id, on_delete=models.CASCADE, related_name='Related Team', null=True)
    created_by = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='Creator', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
