from django.contrib import admin
from tasks.models import task


# Register your models here.
@admin.register(task.Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'status', 'due_to', 'owner', 
    )