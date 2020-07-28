from django.urls import reverse
from rest_framework.test import APITestCase


class TestAccountsSetUp(APITestCase):

    # method calls for all methods that run
    def setUp(self):     

        # all the needed urls with with right and wrong usernames
        self.create_account_url=reverse('create-account')
        self.get_account_url=reverse('get-account', kwargs={'username':'username'})
        self.get_unexisting_account_url=reverse('get-account', kwargs={'username':'unexisting_user_test'})
        self.put_account_url=reverse('put-account', kwargs={'username':'username'})
        self.put_unexisting_account_url=reverse('put-account', kwargs={'username':'unexisting_user_test'})
        self.delete_account_url=reverse('delete-account', kwargs={'username':'username'})
        self.delete_unexisting_account_url=reverse('delete-account', kwargs={'username':'unexisting_user_test'})

        # used username for create
        self.account_data = {
            'username': 'username', 
            'email' : 'email@gmail.com',
            'password': 'password',
            'is_superuser' : False
            }  

        # user with token for testing
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.client.post(self.create_account_url, self.account_data).data['token'])

        return super().setUp()
