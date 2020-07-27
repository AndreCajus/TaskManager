from django.urls import include, path
from account.views import *

urlpatterns = [
    path('create', create_account, name="create-account"),
    path('<username>/', get_account, name="get-account"),
    path('<username>/update', put_account, name="put-account"),
    path('<username>/delete', delete_account, name="delete-account"),
    path('list', ListAccounts.as_view(), name="list-accounts")
]