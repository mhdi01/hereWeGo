import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import datetime
from .models import User, Ads, Comments
from .serializers import RegisterSerializer, AdSerializer, ModifyAdSerializer, CreateCommentSerializer, CommentSerializer

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {'email': 'test@example.com', 'password': 'testpassword'}
        self.invalid_payload = {'email': 'invalid-email', 'password': 'testpassword'}

    def test_valid_registration(self):
        response = self.client.post(reverse('register'), self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_registration(self):
        response = self.client.post(reverse('register'), self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class AdCRUDTestCase(TestCase):
    def setUp(self):
        self.user_data = {'email': 'test@example.com', 'password': '123123333m'}
        response = self.client.post(reverse('register'), self.user_data)
        self.user = User.objects.filter(email=response.json()['email']).first()
        self.ad = Ads.objects.create(title='Test Ad', content='Test Ad Content', user=self.user)
        self.token = self.client.post(reverse('token_obtain_pair'), data=self.user_data).json()
        self.headers = {'Authorization': f'Bearer {self.token["access"]}'}
        
    def test_create_ad(self):
        data = {'title': 'New Ad', 'content': 'New Ad Content', 'user': self.user.id}
        response = self.client.post(reverse('create_ad'), data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_ad(self):
        data = {'title': 'Updated Ad', 'content': 'Updated Ad Content', 'user': self.user.id}
        response = self.client.patch(reverse('update_ad', kwargs={'ad_id': self.ad.id}), data, content_type='application/json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ad(self):
        response = self.client.delete(reverse('delete_ad', kwargs={'ad_id': self.ad.id}), content_type='application/json', headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentTestCase(TestCase):
    def setUp(self):
        self.user_data = {'email': 'test@example.com', 'password': '123123333m'}
        response = self.client.post(reverse('register'), self.user_data)
        self.user = User.objects.filter(email=response.json()['email']).first()
        self.ad = Ads.objects.create(title='Test Ad', content='Test Ad Content', user=self.user)
        self.comment = Comments.objects.create(user=self.user, ad=self.ad, content='Test Comment')
        self.token = self.client.post(reverse('token_obtain_pair'), data=self.user_data).json()
        self.headers = {'Authorization': f'Bearer {self.token["access"]}'}
        

    def test_create_comment(self):
        Comments.objects.filter(user=self.user.id).delete()
        data = {'user': self.user.id, 'ad': self.ad.id, 'content': 'New Comment'}
        response = self.client.post(reverse('create_comment', kwargs={'ad_id': self.ad.id}), data, headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_comments(self):
        response = self.client.get(reverse('list_ad_comments', kwargs={'ad_id': self.ad.id}), headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

