from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializes import *
from .models import *


#Task Model CRUD operations

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_new_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_task(request, task_id):
    try:
        task = Task.objects.all(task_id=task_id)
    except Task.DoesNotExist:
        return Response({'error:': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, task_id):
    try:
        task = Task.objects.all(task_id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response({'message': 'task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


#Category Model CRUD operations

@api_view(['GET'])
def get_categories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_category(request, category_id):
    try:
        category = Category.objects.get(category_id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category, request.data)

    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request, category_id):
    try:
        Category = Category.objects.get(category_id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category Does Not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    Category.delete()
    return Response({'message': 'Category Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)


#Notification Model CRUD operations

@api_view(['GET'])
def get_notifications(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_notification(request):
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_notification(request, notification_id):
    try:
        notification = Notification.objects.get(notification_id=notification_id)
    except Notification.DoesNotExist:
        return Response({'error': 'This notification does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    notification.delete()
    
    return Response({'message': 'Notification deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
