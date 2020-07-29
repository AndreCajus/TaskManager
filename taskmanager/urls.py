from django.urls import include, path
from taskmanager.views import *

urlpatterns = [
    path('create', create_task, name="create-task"),
    path('<int:pk>/', get_task, name="get-task"),
    path('<int:pk>/update', put_task, name="put-task"),
    path('<int:pk>/validate', validate_task, name="validate-task"),
    path('<int:pk>/delete', delete_task, name="delete-task"),
    path('list', ListTasks.as_view(), name="list-tasks"),
    path('invalid/list', ListInvalidTasks.as_view(), name="invalid-list-tasks"),
]