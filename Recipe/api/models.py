from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'recipe'
        ordering = ['id', ]
        verbose_name_plural = 'Recipes'
        verbose_name = 'Recipe'
    
    def __str__(self):
    	return self.name


class Step(models.Model):
    step_text = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        db_table = 'step'
        ordering = ['id', ]
        verbose_name_plural = 'Steps'
        verbose_name = 'Step'

    def __str__(self):
    	return self.step_text    

class Ingredient(models.Model):
    text = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'ingredient'
        ordering = ['id', ]
        verbose_name_plural = 'Ingredients'
        verbose_name = 'Ingredient'

    def __str__(self):
    	return self.text
