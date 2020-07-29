from django.urls import reverse
from rest_framework.test import APITestCase, APIClient


class TestAccountsSetUp(APITestCase):

    # method calls for all methods that run
    def setUp(self):     

        # all the needed urls with with right and wrong usernames
        self.create_account_url=reverse('create-account')
        self.get_account_url=reverse('get-account', kwargs={'username':'admin'})
        self.get_unexisting_account_url=reverse('get-account', kwargs={'username':'unexisting_user_test'})
        self.put_account_url=reverse('put-account', kwargs={'username':'admin'})
        self.put_unexisting_account_url=reverse('put-account', kwargs={'username':'unexisting_user_test'})
        self.delete_account_url=reverse('delete-account', kwargs={'username':'admin'})
        self.delete_unexisting_account_url=reverse('delete-account', kwargs={'username':'unexisting_user_test'})

        # used username for create
        self.account_data = {
            'username': 'admin', 
            'email' : 'email@gmail.com',
            'password': 'password',
            'is_superuser' : True
            }  

        # user with token for testing
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.client.post(self.create_account_url, self.account_data).data['token'])

        # Client 2 - Admin
        self.client2 = APIClient()
        self.user2_data = {
            'username': 'staff', 
            'email' : 'email2@gmail.com',
            'password': 'password2',
            'is_superuser' : False,
            }   
        self.client2.credentials(HTTP_AUTHORIZATION='Token ' + self.client2.post(self.create_account_url, self.user2_data).data['token'])

        return super().setUp()
