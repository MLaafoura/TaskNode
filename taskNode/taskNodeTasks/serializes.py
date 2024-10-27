from rest_framework import serializers
from .models import *
from taskNodeUser.models import CustomUser


class UserTaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = UserTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    users = UserTaskSerializer(many=True, write_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        task = Task.objects.create(**validated_data)

        for user_data in users_data:
            UserTask.objects.create(
                user=user_data['user'],
                task=task,
                role=user_data['role'],
            )


class CategorySerializer(serializers.ModelSerializer):
    related_category = TaskSerializer(read_only=True, many=True, source='related_category')

    class Meta:
        model = Category
        exclude = ['category_id']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        