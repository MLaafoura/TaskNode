from django.db import models
from taskNodeUser.models import CustomUser
from taskNodeTeams.models import Team
from taskNodeProjects.models import Project


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    created_at = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='Related User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()


PRIORITIES = [
    ('LOW', 'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH', 'High')

]

STATUS = [
    ('TO-DO', 'To-Do'),
    ('IN_PROGRESS', 'In progress'),
    ('COMPLETED', 'Completed')
]

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=255)
    priority = models.CharField(choices=PRIORITIES, max_length=255)
    deadline = models.DateTimeField()
    project_id = models.ForeignKey(Project.project_id, on_delete=models.CASCADE, related_name='Related Project', null=True)
    category_id = models.ForeignKey(Category.category_id, on_delete=models.CASCADE, related_name='Related Category', null=True)
    team_id = models.ForeignKey(Team.team_id, on_delete=models.CASCADE, related_name='Related Team', null=True)
    created_by = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()


ROLES = [
    ('ASSIGNEE', 'Assignee'),
    ('REVIEWER', 'Reviewer'),
    ('OWNER', 'Owner')
]


class UserTask(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task.task_id, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, max_length=255)
    assigned_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task.task_id, on_delete=models.CASCADE, related_name='Related Task')
    user_id = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='Related User')
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser.id, on_delete=models.CASCADE, related_name='Related User')
    task_id = models.ForeignKey(Task.task_id, on_delete=models.CASCADE, related_name='Related Task')
    message = models.TextField(max_length=2000)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)   
