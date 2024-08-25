"""This module contains the task api views."""
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from alxfocuszen_engine.api.v1.engine.task_serializer import TaskSerializer
from alxfocuszen_engine.models.tasks import Task
from alxfocuszen_engine.models.user import UserProfile


class TaskListView(generics.ListCreateAPIView):
    """This class defines the view for listing and creating tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """This method creates a new task.
        
        Args:
            serializer (TaskSerializer): The task serializer object.
        """
        if Task.objects.filter(user=self.request.user, title=serializer.validated_data['title'],
                               due_date=serializer.validated_data['due_date']).exists():
            raise ValidationError("You already have a task with the same title and due date.")
        serializer.save(user=self.request.user)


    def get_queryset(self):
        """This method filters the tasks based on the user.
        
        Returns:
            QuerySet: The queryset of tasks.
        """
        return Task.objects.filter(user=self.request.user)
    

    def list(self, request, *args, **kwargs):
        """This method lists the tasks.
        
        Args:
            request (Request): The request object.
        
        Returns:
            Response: The response with the tasks data.
        """
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)