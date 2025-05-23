import json
from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, encoding='utf-8') as f:
            ingredients = json.load(f)

        for ingredient in ingredients:
            Ingredient.objects.get_or_create(
                name=ingredient['name'],
                measurement_unit=ingredient['measurement_unit']
            )
