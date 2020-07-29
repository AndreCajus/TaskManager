from rest_framework import status
from .tests_setup import TestAccountsSetUp


class TestUpdateAccountAPI(TestAccountsSetUp):

    def test_put_existing_account(self):
        response = self.client.put(self.put_account_url, self.account_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


    def test_put_existing_account_missing_parameters(self):
        response = self.client.put(self.put_account_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.content)


    def test_put_unexisting_account(self):
        response = self.client.put(self.put_unexisting_account_url, self.account_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.content)


    def test_put_existing_account_with_unauthorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.put(self.put_account_url, self.account_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)


    def test_put_nonadmin_on_other_accout(self):
        response = self.client2.put(self.put_account_url, self.account_data) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)
