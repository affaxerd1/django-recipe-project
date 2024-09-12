""" Test recipe API """
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe
from recipe.serializers import RecipeSerializer

def create_recipe(use, **params):
    """create and return a sample recipe"""
    defaults = {
        'title' : "Sample recipe title",
        'time_minutes' : 10,
        'price': Decimal('5.25'),
        'description': 'Sample recipe description',
        'link': 'https://samplelink.com'
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe

