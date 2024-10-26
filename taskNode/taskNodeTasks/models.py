from django.db import models
from taskNodeUser.models import CustomUser
from taskNodeTeams.models import Team
from taskNodeProjects.models import Project


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='related_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='related_project', null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='related_category', null=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='related_team', null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}, {self.status}'
    
    class Meta:
        ordering = ('title', 'status')

ROLES = [
    ('ASSIGNEE', 'Assignee'),
    ('REVIEWER', 'Reviewer'),
    ('OWNER', 'Owner')
]


class UserTask(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, max_length=255)
    assigned_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_comment')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_comment')
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_notification')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_notification')
    message = models.TextField(max_length=2000)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)   
