from common.views.mixins import LCRUDViewSet
from tasks.models.task import Task
from tasks.serializers.api.tasks import TaskListSerializer, TaskDetailSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from tasks.filters import TaskFilter


@extend_schema_view(
    list=extend_schema(summary='Список Задач', tags=['Задачи']),
    retrieve=extend_schema(summary='Детально о задаче', tags=['Задачи']),
    create=extend_schema(summary='Создать задачу', tags=['Задачи']),
    update=extend_schema(summary='Изменить задачу', tags=['Задачи']),
    partial_update=extend_schema(summary='Изменить задачу частично', tags=['Задачи']),
    destroy=extend_schema(summary='Удалить задачу', tags=['Задачи']),
)
class TasksModelView(LCRUDViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = TaskFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'created', 'due_to',)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update', 'retrieve', 'create']:
            return TaskDetailSerializer
        return self.serializer_class
    
    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)
        return queryset

    