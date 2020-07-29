from rest_framework import status
from .tests_setup import TestTasksSetUp
from django.urls import reverse
from taskmanager.models import Task

class TestUpdateTaskAPI(TestTasksSetUp):

    def test_put_existing_task(self):
        response = self.client.put(self.put_task_url, self.task_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_put_existing_task_missing_parameters(self):
        response = self.client.put(self.put_task_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)

    def test_put_unexisting_task(self):
        response = self.client.put(self.put_unexisting_task_url, self.task_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.content)

    def test_put_existing_task_with_unauthorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.put(self.put_task_url, self.task_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)

    # shouldnt be possible, only admins can update states
    def test_staff_put_task_with_state(self):
        self.client2.post(self.create_task_url, self.task_data)
        response = self.client2.put(self.put_task_url,
                                    {'id' : self.task_id,
                                    'description' : 'teste',
                                    'states': Task.States.RESOLVED})
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 

    # should be possible, admins can update states
    def test_admin_put_task_with_state(self):
        self.client2.post(self.create_task_url, self.task_data)
        response = self.client.put(self.put_task_url,
                                    {'id' : self.task_id,
                                    'description' : 'teste',
                                    'states': Task.States.RESOLVED})
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    # if staff updates existing verified state, state should become not verified
    def test_staff_put_task_auto_update_state_to_validate(self):
        # put with status "Resolved"
        self.client.put(self.put_task_url,
                                    {'id' : self.task_id,
                                    'description' : 'teste',
                                    'states': Task.States.RESOLVED})
        # update without status
        self.client2.put(self.put_task_url, {'description' : 'teste2'})
        r = self.client2.get(self.get_task_url, {'id' : self.task_id})
        # status should automatically update to "To Validate"
        self.assertEqual(r.data['states'], Task.States.TO_VALIDATE) 
