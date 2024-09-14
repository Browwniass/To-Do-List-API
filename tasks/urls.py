from django.urls import include, path
from tasks.views.tasks import TasksModelView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'tasks', TasksModelView), 'tasks'

urlpatterns = [
    path('', include(router.urls))    
]
