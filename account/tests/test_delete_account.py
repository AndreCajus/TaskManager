from django.urls import reverse
from rest_framework import status
from .tests_setup import TestAccountsSetUp


class TestDeleteAccountAPI(TestAccountsSetUp):

    def test_delete_existing_account(self):
        response = self.client.delete(self.delete_account_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


    def test_delete_unexisting_account(self):
        response = self.client.delete(self.delete_unexisting_account_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND, response.content)

    
    def test_admin_delete_other_account(self):
        # client = superuser, delete_account is related to the NO admin user
        response = self.client.delete(reverse('delete-account', kwargs={'username':'staff'})) 
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
    
    
    def test_nonadmin_delete_other_account(self):
        # client2 = normal user, user admin is related to client
        response = self.client2.delete(self.delete_account_url) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)
  

    def test_delete_account_with_unauthorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.delete(self.delete_account_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.content)
