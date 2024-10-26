from django.urls import path
from .views import (
        TaskListView, 
        TaskDetailView, 
        CategoryListView, 
        CategoryDetailView, 
        NotificationListView, 
        NotificationDetailView,
        )


urlpatterns = [
    path('', TaskListView.as_view(),name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-details'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-details'),
    path('notification/', NotificationListView.as_view(), name='notification-list'),
    path('notification/<int:pk>/', NotificationDetailView.as_view(), name='notification-details')

]