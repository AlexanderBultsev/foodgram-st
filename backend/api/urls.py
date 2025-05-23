from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, IngredientViewSet, RecipeViewSet, redirect_short_link
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('s/<str:code>/', redirect_short_link, name='short_link'),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
