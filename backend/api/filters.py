from django_filters.rest_framework import FilterSet, filters

from recipes.models import Recipe, User


class RecipeFilter(FilterSet):
    author = filters.ModelChoiceFilter(
        queryset=User.objects.all(),
    )

    is_in_shopping_cart = filters.NumberFilter(
        method='filter_is_in_shopping_cart',
    )

    is_favorited = filters.NumberFilter(
        method='filter_is_favorited',
    )

    def filter_is_favorited(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(favorited_by__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if self.request.user.is_authenticated and value:
            return queryset.filter(in_carts__user=self.request.user)
        return queryset

    class Meta:
        model = Recipe
        fields = (
            'author',
            'is_in_shopping_cart',
            'is_favorited',
        )
