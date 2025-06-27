'''This module defines a Recipe class that represents a recipe object.'''

import ast

class Recipe():
    '''This class represents a recipe object. It contains methods to get the title, 
    ingredients, and instructions of the recipe.'''

    def __init__(self, recipe_id, recipe_title, recipe_instructions=None, recipe_ingredients=None):
        '''Constructor that initializes the recipe object with the given recipe data.'''
        self.recipe_id = recipe_id
        self.title = recipe_title
        if recipe_instructions is not None:
            self.instructions = recipe_instructions.split("\n")
        else:
            self.instructions = recipe_instructions
        if recipe_ingredients is not None:
            self.ingredients = ast.literal_eval(recipe_ingredients)
        else:
            self.ingredients = recipe_ingredients

    def get_id(self):
        '''Returns the ID of the recipe.'''
        return self.recipe_id

    def get_title(self):
        '''Returns the title of the recipe.'''
        return self.title

    def get_instructions(self):
        '''Returns the instructions of the recipe.'''
        return self.instructions

    def get_ingredients(self):
        '''Returns the ingredients of the recipe.'''
        return self.ingredients
