from django.contrib import admin
from .models import Task, Category, UserTask, Comment, Notification


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'priority', 'created_by')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_by', 'updated_at')


@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'task_id', 'role', 'assigned_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'task_id', 'created_at')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'task_id', 'created_at')