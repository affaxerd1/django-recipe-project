"""
Tets for the tag API
"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from yaml import serialize

from core.models import Tag

from recipe.serializers import TagSerializer

TAGS_URL = reverse('recipe:tag-list')

def create_user(email="user@example.com", password="test123"):
    """create and return a user"""
    return get_user_model().objects.create_user(email=email, password = password)

class PublicTagsApiTets(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateTagsApiTests(TestCase):
    """Test authenticated API requests"""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
       """Tets retrieving a list of tags"""
       Tag.objects.create(user=self.user, name="vegan" )
       Tag.objects.create(user=self.user, name="Dessert")

       res = self.client.get(TAGS_URL)

       tags= Tag.objects.all().order_by('-name')
       serializer=TagSerializer(tags, many=True)
       self.assertEqual(res.status_code, status.HTTP_200_OK)
       self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test list of tags is limited to authenticated user"""
        user2 = create_user(email="user2@example.com", password="test123")
        Tag.objects.create(user=user2, name='Fruity')
        tag = Tag.objects.create(user=self.user, name ='Comfort food')

        res = self.client.get(tag)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0],['name'], tag.name)

