'''This module contains the DataSource class that handles database connections and queries.'''

import sys
import psycopg2
import ProductionCode.psql_config as config
from ProductionCode.recipe import Recipe
from ProductionCode.datasource_meta import DataSourceMeta

class DataSource(metaclass=DataSourceMeta):
    '''This class handles the connection to the PostgreSQL database 
    and provides methods to query recipes.'''

    def __init__(self):
        '''Constructor that initiates connection to database'''
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object.'''

        try:
            connection = psycopg2.connect(database=config.DATABASE,
                                          user=config.USER,
                                          password=config.PASSWORD,
                                          host="localhost")
        except psycopg2.Error as e:
            print("Connection error: ", e)
            sys.exit(1)
        return connection

    def get_all_recipes(self):
        '''Returns all recipes from the database'''
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, title FROM recipe ORDER BY title")
        records = [self.convert_recipe_to_object(record) for record in cursor.fetchall()]
        cursor.close()

        return records

    def get_recipe_by_ingredients(self, include_ingredients, exclude_ingredients):
        '''Fetches recipes that include certain ingredients and exclude others'''
        cursor = self.connection.cursor()

        query = self.generate_ingredients_query(include_ingredients, exclude_ingredients)

        if query:
            cursor.execute(query)
            records = [self.convert_recipe_to_object(record) for record in cursor.fetchall()]
            cursor.close()
            return records
        return []

    def generate_ingredients_query(self, include_ingredients, exclude_ingredients):
        '''Generates the WHERE clause for the ingredients query'''
        query_separated = []

        if include_ingredients:
            query_separated.extend([f"ingredients ILIKE '%{ingredient}%'"
                               for ingredient in include_ingredients])

        if exclude_ingredients:
            query_separated.extend([f"ingredients NOT ILIKE '%{ingredient}%'"
                               for ingredient in exclude_ingredients])

        if query_separated:
            final_query = "SELECT * FROM recipe WHERE "
            final_query += " AND ".join(query_separated)
            final_query += " ORDER BY title;"
            return final_query
        return None



    def get_random_recipes(self, number):
        ''' This function retrieves random recipes from the database.
        Args:
        number: number of random recipes to retrieve
        Returns a list of tuples containing the data.
        '''
        query = "SELECT * FROM recipe ORDER BY RANDOM() LIMIT %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (number,))
        records = [self.convert_recipe_to_object(record) for record in cursor.fetchall()]
        cursor.close()
        return records

    def get_recipe_by_title(self, title):
        '''This function retrieves the recipe ID based on the recipe title.
        Args:
        title: title of the recipe
        Returns the recipe ID.
        '''

        exact_match = self.get_exact_match(title)
        if exact_match:
            return [exact_match]

        close_matches = self.get_recipes_containing_title(title)
        return close_matches

    def get_exact_match(self, title):
        '''This function retrieves the recipe data based on the exact title match.'''

        cursor = self.connection.cursor()
        query = "SELECT * FROM recipe WHERE title = %s"
        cursor.execute(query, (title,))
        result = cursor.fetchone()
        recipe = self.convert_recipe_to_object(result)
        cursor.close()
        return recipe

    def get_recipes_containing_title(self, title):
        '''This function retrieves recipes that contain the given title.'''

        cursor = self.connection.cursor()
        query = "SELECT * FROM recipe WHERE title ILIKE %s"
        cursor.execute(query, (f"%{title}%",))
        recipes = [self.convert_recipe_to_object(record) for record in cursor.fetchall()]
        cursor.close()
        return recipes


    def convert_recipe_to_object(self, recipe):
        '''This function converts the recipe data into a Recipe object.
        Args:
        recipe: tuple containing the recipe data
        Returns a Recipe object.
        '''

        if recipe:
            if len(recipe) == 2:
                recipe_id, title = recipe
                return Recipe(recipe_id, title)
            if len(recipe) == 4:
                recipe_id, title, instructions, ingredients = recipe
                return Recipe(recipe_id, title, instructions, ingredients)
        return None

    def get_recipe_by_id(self, recipe_id):
        '''This function retrieves the recipe data based on the recipe ID.
        Args:
        recipe_id: ID of the recipe
        Returns the recipe data.
        '''
        cursor = self.connection.cursor()
        query = "SELECT * FROM recipe WHERE id = %s"
        cursor.execute(query, (recipe_id,))
        recipe = self.convert_recipe_to_object(cursor.fetchone())
        cursor.close()
        return recipe

    def get_all_recipe_titles(self):
        '''This function retrieves all recipe titles from the database.
        Returns a list of recipe titles.
        '''
        cursor = self.connection.cursor()
        query = "SELECT title FROM recipe"
        cursor.execute(query)
        titles = cursor.fetchall()
        cursor.close()
        return [title[0] for title in titles]
