from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Receipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class StepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Steps to be viewed or edited.
    """
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class Recipe_by_user_view(RetrieveAPIView):
    """
    API endpoint that allows to retrieve recipe by user id.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().filter(user=self.get_object())
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

class Recipe_by_username_view(RetrieveAPIView):
    """
    API endpoint that allows to retrieve recipe by username.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def retrieve(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().filter(user=self.get_object())
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
