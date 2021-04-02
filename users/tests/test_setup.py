from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from model_mommy import mommy

from django.conf import settings

User = settings.AUTH_USER_MODEL


class TestSetUp(APITestCase):

    def setUp(self):
        # self.register_url = reverse('register')
        self.client = APIClient()
        self.register_url = 'auth/registration/'
        self.login_url = reverse('login')
        self.user_a = mommy.make('users.User')

        self.user_data = {
            'email': 'testuseremail@gmail.com',
            'username': 'testuserusername',
            'password1': 'Testpassword123123',
            'password2': 'Testpassword123123'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
