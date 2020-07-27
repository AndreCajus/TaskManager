from .tests_setup import TestAccountsSetUp
from rest_framework import status
import time  

class TestCreateAccountAPI(TestAccountsSetUp):
   
    post_account = {'username':'postuser', 'password' : 'postpassword', 
                    'email' : 'postemail@gmail.com'}

    def test_create_account_mandatory_parameters(self):
        response = self.client.post(self.create_account_url, self.post_account)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  


    def test_create_account_with_some_possibilities(self):
        combinations = {
            'upe' : {'username':'username1', 'password' : 'password1', 
                    'email' : 'testeemail@gmail.com1'},
            'upef' : {'username':'username2', 'password' : 'password2', 
                    'email' : 'testeemail@gmail.com2', 'first_name' : 'andre2'},
            'all'  : {'username':'username3', 'password' : 'password3', 
                    'email' : 'testeemail@gmail.com3', 'first_name' : 'andre3',
                    'last_name': 'lastname3', 'is_staff' : 'True', 'is_active' : True,
                    'is_superuser' : True, 'last_login' : time.strftime('2000-12-22 22:30:59'),
                    'date_joined' : time.strftime('1999-12-22 22:30:59')},
        }
        for k, v in combinations.items():
            try:
                response = self.client.post(self.create_account_url, v)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)        
            except:
                self.assertEqual(status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST)


    def test_create_account_missing_parameters(self):
        response = self.client.post(self.create_account_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)    


    def test_create_account_wrong_email(self):
        self.account_data['email'] = "wrong_email_string"
        response = self.client.post(self.create_account_url, self.account_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 


    def test_create_account_token_correctly_generated(self):
        response = self.client.post(self.create_account_url, self.post_account)
        self.assertTrue('token' in response.data)