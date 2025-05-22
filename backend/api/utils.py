from django.db.models import Sum
from django.http import HttpResponse
import os
from hashids import Hashids

from recipes.models import Cart, RecipeIngredient


hashids = Hashids(min_length=6, salt=os.getenv("DJANGO_SECRET_KEY"))


def encode_recipe_id(recipe_id: int) -> str:
    return hashids.encode(recipe_id)


def decode_recipe_code(code: str) -> int:
    decoded = hashids.decode(code)
    return decoded[0] if decoded else None


def shopping_cart(user):
    recipe_ids = Cart.objects.filter(
        user=user).values_list('recipe_id', flat=True)

    sum_ingredient = RecipeIngredient.objects.filter(
        recipe__in=recipe_ids
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(
        amount=Sum('amount')
    ).order_by('ingredient__name')

    ingredient_list = 'Список покупок\n\n'
    for ingredient in sum_ingredient:
        ingredient_list += (
            f'{ingredient["ingredient__name"]} - '
            f'{ingredient["amount"]} '
            f'({ingredient["ingredient__measurement_unit"]})\n'
        )

    response = HttpResponse(ingredient_list, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=shopping_cart.txt'
    return response
