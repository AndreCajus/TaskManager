from rest_framework import status
from .tests_setup import TestTasksSetUp


class TestDeleteTaskAPI(TestTasksSetUp):

    def test_delete_existing_task(self):
        response = self.client.delete(self.delete_task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_delete_unexisting_task(self):
        response = self.client.delete(self.delete_unexisting_task_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.content)

    def test_delete_task_with_unauthorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.delete(self.delete_task_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)
