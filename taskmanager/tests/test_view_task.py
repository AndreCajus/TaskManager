from rest_framework import status
from .tests_setup import TestTasksSetUp


class TestViewTasksAPI(TestTasksSetUp):

    def test_view_existing_task(self):
        response = self.client.get(self.get_task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

    def test_view_unexisting_account(self):
        response = self.client.get(self.get_unexisting_task_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.content)

    def test_view_existing_account_with_unauthorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(self.get_task_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)
