from .tests_setup import TestTasksSetUp
from rest_framework import status

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