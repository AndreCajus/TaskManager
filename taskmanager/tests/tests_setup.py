from django.urls import reverse
from rest_framework.test import APITestCase


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

        # create user to be used
        self.create_account_url=reverse('create-account')
        self.user_data = {
            'username': 'username', 
            'email' : 'email@gmail.com',
            'password': 'password'
            }   
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.client.post(self.create_account_url, self.user_data).data['token'])

        # create task to be used
        self.task_data = {
            'description': 'test_task', 
            }   
        self.client.post(self.create_task_url, self.task_data)
        
        return super().setUp()
