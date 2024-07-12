"""This module contains the task api views."""
from rest_framework import status, generics
from rest_framework.response import Response
from alxfocuszen_engine.api.v1.engine.task_serializer import TaskSerializer
from alxfocuszen_engine.models.tasks import Task


class TaskListView(generics.ListCreateAPIView):
    """This class defines the view for listing and creating tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """This method creates a new task.
        
        Args:
            serializer (TaskSerializer): The task serializer object.
        """
        serializer.save(user=self.request.user.id)


    def get_queryset(self):
        """This method filters the tasks based on the user.
        
        Returns:
            QuerySet: The queryset of tasks.
        """
        return Task.objects.filter(user=self.request.user.id)
    

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