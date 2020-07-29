import time
from rest_framework import status
from .tests_setup import TestTasksSetUp
from taskmanager.models import Task


class TestCreateTaskAPI(TestTasksSetUp):
   
    post_task = {'description': 'posttest'} 

    def test_create_task_mandatory_parameters(self):
        response = self.client.post(self.create_task_url, self.post_task)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  

    def test_create_task_missing_parameters(self):
        response = self.client.post(self.create_task_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)    

    def test_create_task_wrong_category(self):
        self.post_task['category'] = "wrong_category"
        response = self.client.post(self.create_task_url, self.post_task)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # shouldnt be possible, only admins can update states
    def test_staff_create_task_with_state(self):
        response = self.client2.post(self.create_task_url,
                                    {'description': 'test_task', 
                                    'states': Task.States.RESOLVED})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 

    # should be possible, admins can update states
    def test_admin_create_task_with_state(self):
        response = self.client.post(self.create_task_url,
                                    {'description': 'test_task2', 
                                    'states': Task.States.RESOLVED})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 