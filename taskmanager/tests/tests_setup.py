from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from taskmanager.models import Task
from django.contrib.auth.models import User
import json


class TestTasksSetUp(APITestCase):

    # method calls for all methods that run
    def setUp(self):    

        # to make tas creation possible
        self.create_task_url=reverse('create-task')

        # Client 1 - Admin client
        self.create_account_url=reverse('create-account')
        self.user_data = {
            'username': 'admin', 
            'email' : 'email@gmail.com',
            'password': 'password',
            'is_superuser' : True,
            }   
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.client.post(self.create_account_url, self.user_data).data['token'])

        # Client 2 - Not an Admin Client
        self.client2 = APIClient()
        self.user2_data = {
            'username': 'staff', 
            'email' : 'email2@gmail.com',
            'password': 'password2',
            'is_superuser' : False,
            }   
        self.client2.credentials(HTTP_AUTHORIZATION='Token ' + self.client2.post(self.create_account_url, self.user2_data).data['token'])

        # create a task and get its id
        self.task_data = {
            'description':'testetask'
            }
        self.client.post(self.create_task_url, self.task_data)
        self.task_id = Task.objects.filter(description='testetask').values_list('id', flat=True)[0]

        self.non_existing_id = 404
        # all the needed urls with with right and wrong ids
        self.get_task_url=reverse('get-task', kwargs={'pk': self.task_id})
        self.get_unexisting_task_url=reverse('get-task', kwargs={'pk': self.non_existing_id})
        self.put_task_url=reverse('put-task', kwargs={'pk': self.task_id})
        self.put_unexisting_task_url=reverse('put-task', kwargs={'pk': self.non_existing_id})
        self.delete_task_url=reverse('delete-task', kwargs={'pk': self.task_id})
        self.delete_unexisting_task_url=reverse('delete-task', kwargs={'pk': self.non_existing_id})

        return super().setUp()
