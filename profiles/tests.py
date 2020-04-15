from django.shortcuts import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Profile


post_get_url = reverse('all-profiles')


def get_post_put_delete_url(pk):
    return reverse('profile', kwargs={'pk': pk})


def get_profile_pk():
    return Profile.objects.first().pk


class GetProfilesTest(APITestCase):

    def setUp(self):
        user_1 = {'username': 'user1', 'password': 'test-password123'}
        user_2 = {'username': 'user2', 'password': 'test-password456'}
        # create a new users with a post request to djoser endpoint
        self.user = self.client.post('/auth/users/', data=user_1)
        self.user = self.client.post('/auth/users/', data=user_2)

    def test_profile_get_all(self):
        """Test retrieving all profile with get request"""
        response = self.client.get(post_get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_profile_get_single(self):
        """Test retrieving single profile with get request"""
        pk = get_profile_pk()
        response = self.client.get(reverse('profile', kwargs={'pk': pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner'], 'user1')


class UpdateProfilesTest(APITestCase):
    def setUp(self):
        user_1 = {'username': 'user1', 'password': 'test-password123'}
        self.user = self.client.post('/auth/users/', data=user_1)
        response = self.client.post('/auth/jwt/create/', data=user_1)
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_profile_put_authenticated(self):
        """Test updating profile by authenticated user"""
        pk = get_profile_pk()
        url = reverse('profile', kwargs={'pk': pk})
        profile_data = {'description': 'test profile', 'country': 'ABC', 'city': 'A'}
        response = self.client.put(url, profile_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.get(pk=pk).city, 'A')

    def test_profile_put_unauthenticated(self):
        """Test updating profile by unauthenticated user"""
        pk = get_profile_pk()
        url = reverse('profile', kwargs={'pk': pk})
        profile_data = {'description': 'test profile', 'country': 'ABC', 'city': 'A'}
        self.client.logout()
        response = self.client.put(url, profile_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class DeleteProfilesTest(APITestCase):
    def setUp(self):
        user_1 = {'username': 'user1', 'password': 'test-password123'}
        self.user = self.client.post('/auth/users/', data=user_1)
        response = self.client.post('/auth/jwt/create/', data=user_1)
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_profile_delete_authenticated(self):
        """Test deleting profile by authenticated user"""
        pk = get_profile_pk()
        url = get_post_put_delete_url(pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(bool(Profile.objects.all()))

    def test_profile_delete_unauthenticated(self):
        """Test deleting profile by unauthenticated user"""
        pk = get_profile_pk()
        url = get_post_put_delete_url(pk)
        self.client.logout()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CreateProfilesTest(APITestCase):
    def setUp(self):
        user_data = {'username': 'test_user', 'password': 'test-password123'}
        self.user = self.client.post('/auth/users/', data=user_data)
        response = self.client.post('/auth/jwt/create/', data=user_data)
        self.token = response.data['access']
        self.api_authentication()
        pk = get_profile_pk()
        url = get_post_put_delete_url(pk)
        # By default profiles are created after registrations,
        # so to test profile creation let's delete it first
        self.client.delete(url)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_profile_post_authenticated(self):
        """Test profile creation by authenticated user"""
        profile_data = {'description': 'test profile', 'country': 'CDE', 'city': 'B'}
        response = self.client.post(post_get_url, profile_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.first().city, 'B')

    def test_profile_post_unauthenticated(self):
        """Test profile creation by unauthenticated user"""
        profile_data = {'description': 'test profile', 'country': 'CDE', 'city': 'B'}
        self.client.logout()
        response = self.client.post(post_get_url, profile_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
