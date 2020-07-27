import time
from rest_framework import status
from .tests_setup import TestTasksSetUp


class TestCreateTaskAPI(TestTasksSetUp):
   
    post_task = {'description': 'post_task'} 

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
