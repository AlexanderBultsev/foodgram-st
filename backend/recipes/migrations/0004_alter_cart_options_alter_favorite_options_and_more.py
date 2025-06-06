# Generated by Django 5.2 on 2025-05-29 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_cart_recipe_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': [
                'recipe'], 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': [
                'recipe'], 'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'ordering': ['recipe'], 'verbose_name': 'Ингредиент в рецепте',
                     'verbose_name_plural': 'Ингредиенты в рецепте'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(
                1), django.core.validators.MaxValueValidator(32000)], verbose_name='Время приготовления (в минутах)'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(
                1), django.core.validators.MaxValueValidator(32000)], verbose_name='Количество'),
        ),
    ]
