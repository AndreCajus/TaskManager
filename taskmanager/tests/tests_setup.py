from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class TestTasksSetUp(APITestCase):

    # method calls for all methods that run
    def setUp(self):     

        # all the needed urls with with right and wrong usernames
        self.create_task_url=reverse('create-task')
        self.get_task_url=reverse('get-task', kwargs={'description':'test_task'})
        self.get_unexisting_task_url=reverse('get-task', kwargs={'description':'unexisting_test_task'})
        self.put_task_url=reverse('put-task', kwargs={'description':'test_task'})
        self.put_unexisting_task_url=reverse('put-task', kwargs={'description':'unexisting_test_task'})
        self.delete_task_url=reverse('delete-task', kwargs={'description':'test_task'})
        self.delete_unexisting_task_url=reverse('delete-task', kwargs={'description':'unexisting_test_task'})

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

        # create task to be used
        self.task_data = {
            'description': 'test_task', 
            }   
        self.client.post(self.create_task_url, self.task_data)
        
        return super().setUp()
