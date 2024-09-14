from django_filters.rest_framework import FilterSet
from tasks.models.task import Task
import django_filters 


class TaskFilter(FilterSet):
    #status = django_filters.BooleanFilter(field_name='status', label='Статус')
    
    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'created': ['exact', 'gt', 'lt'],
            'due_to': ['exact', 'gt', 'lt'],
        }