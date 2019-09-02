from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recipes', views.RecipeViewSet, 'recipes')
router.register(r'steps', views.StepViewSet, 'steps')
router.register(r'ingredients', views.IngredientViewSet, 'ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='login')),
    path('recipe-by-user/<int:pk>', views.Recipe_by_user_view.as_view()),
    path('recipe-by-username/<str:username>', views.Recipe_by_username_view.as_view())
]