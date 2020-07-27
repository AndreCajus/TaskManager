from django.urls import include, path
from taskmanager.views import *

urlpatterns = [
    path('create', create_task, name="create-task"),
    path('<description>/', get_task, name="get-task"),
    path('<description>/update', put_task, name="put-task"),
    path('<description>/validate', validate_task, name="validate-task"),
    path('<description>/delete', delete_task, name="delete-task"),
    path('list', ListTasks.as_view(), name="list-tasks"),
    path('invalid/list', ListInvalidTasks.as_view(), name="invalid-list-tasks"),
]