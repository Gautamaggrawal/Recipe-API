from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    
    password = serializers.CharField(
            min_length=8,
            write_only=True,
            required=True,
            style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name', 'password']

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Step
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredient
        fields = '__all__'
