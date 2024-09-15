from django_filters.rest_framework import FilterSet
from tasks.models.task import Task


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'created': ['exact', 'gt', 'lt'],
            'due_to': ['exact', 'gt', 'lt'],
        }