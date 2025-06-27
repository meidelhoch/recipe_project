'''
This is the main file for the Flask web application.
It handles the routing and serves the web pages.
'''

import string
import re
from flask import Flask, render_template, request, redirect, url_for, jsonify
from ProductionCode.datasource import DataSource


app = Flask(__name__)

TOTAL_NUM_RECIPES = 13493

@app.route('/')
def homepage():
    '''This function returns the homepage.'''
    recipe_data = DataSource()
    featured_recipe = recipe_data.get_random_recipes(1)
    marc_recipe = recipe_data.get_recipe_by_id(13442)
    willan_recipe = recipe_data.get_recipe_by_id(3606)
    anika_recipe = recipe_data.get_recipe_by_id(5895)
    allison_recipe = recipe_data.get_recipe_by_id(1260)
    return render_template('homepage.html', featured_recipe=featured_recipe[0],
                           marc_recipe=marc_recipe,
                           willan_recipe=willan_recipe,
                           anika_recipe=anika_recipe,
                           allison_recipe=allison_recipe)

@app.route('/big_toast')
def big_toast():
    '''This function returns the big toast page.'''
    return render_template('big_toast.html')

@app.route('/random')
def random(last_search=None):
    '''This function returns the random recipe search page.'''
    return render_template('random.html', last_search=last_search)

@app.route('/handle_random_form', methods=['POST'])
def handle_random_form():
    '''This function handles the random recipe search form submission.
    It generates a certain number of random recipe based on the number of recipes requested.
    Arguments:
        None
    Returns:
        Redirects to the random route with the last search.
    '''
    num = request.form.get('num_recipes')
    recipe_data = DataSource()

    if is_valid_number(num):
        num = int(num)
        recipes = recipe_data.get_random_recipes(num)
        simplified_recipes = [get_id_and_title(recipe) for recipe in recipes]
        return render_template('recipelist.html', recipes=simplified_recipes)

    return random(num)

def get_id_and_title(recipe):
    '''This function returns the ID and title of a recipe.'''
    recipe_info = (recipe.get_id(), recipe.get_title())
    return recipe_info

def is_valid_number(num):
    '''This function checks if the number is valid.'''
    if num.isdigit():
        num = int(num)
        if num < 1 or num > TOTAL_NUM_RECIPES:
            return False
        return True
    return False


@app.route('/ingredient_search', methods=['GET', 'POST'])
def ingredient_search():
    '''Route to display the ingredient search page from ingredient_search.html'''
    return render_template('ingredient_search.html')

@app.route('/handle_ingredient_search', methods=['POST'])
def handle_ingredient_search():
    """Handle ingredient search form submission"""

    recipe_data = DataSource()

    include_ingredients = parse_ingredients(request.form.get('include_ingredients', ''))
    exclude_ingredients = parse_ingredients(request.form.get('exclude_ingredients', ''))

    recipes = recipe_data.get_recipe_by_ingredients(include_ingredients, exclude_ingredients)
    if recipes:
        sorted_recipes = sort_recipes_alphabetically(recipes)
        return render_template('custom_recipes_results.html',
                                sorted_recipes=sorted_recipes,
                                letters=string.ascii_uppercase,
                                highlight=None,
                                included_ingredients=include_ingredients,
                                excluded_ingredients=exclude_ingredients)

    return render_template('no_recipes_found.html',
                            included_ingredients=include_ingredients,
                            excluded_ingredients=exclude_ingredients)

def parse_ingredients(ingredients):
    '''This function parses the ingredients from a string into a list.'''
    parsed_ingredients = []
    if ingredients.strip():
        for ingredient in ingredients.split(','):
            parsed_ingredients.append(ingredient.strip().lower())

    return parsed_ingredients

@app.route('/all_recipes')
def all_recipes():
    '''Route to display all recipes using all_recipes.html
    Arguments:
        None
    Returns:
        Renders the all recipes template with the sorted list of recipes.
    '''

    recipe_data = DataSource()
    recipes = recipe_data.get_all_recipes()
    sorted_recipes = sort_recipes_alphabetically(recipes)
    return render_template('all_recipes.html',
                           sorted_recipes = sorted_recipes,
                           letters = string.ascii_uppercase,
                           highlight = "highlight")

def sort_recipes_alphabetically(recipes):
    '''This function sorts the recipes into buckets for each letter in the alphabet by title.

    Arguments:
        recipes: A list of Recipe objects to be sorted.
    Returns:
        A list of tuples containing the corresponding letter and a list of 
        recipe IDs and titles for all recipes that start with that letter.
    '''
    sorted_recipes = {}
    for letter in string.ascii_uppercase:
        current_letter = []
        sorted_recipes[letter] = current_letter

    for recipe in recipes:
        title = recipe.get_title()
        first_letter = first_alphabetical_character(title)
        sorted_recipes[first_letter.upper()].append((recipe.get_id(), title))

    return sorted_recipes

def first_alphabetical_character(recipe_title):
    '''This function returns the first alphabetical character in a string.'''
    match = re.search(r'[a-zA-Z]', recipe_title)
    return match.group(0) if match else None

@app.route('/search_by_title')
def search_by_title(last_search=None):
    '''Route to display the search by title page from search_by_title.html
    Arguments: 
        last_search: The last searched recipe title which is None unless the last search did not 
        exist in the database.
    Returns:
        Renders the search by title template.
    '''
    return render_template('search_by_title.html', last_search=last_search)

@app.route('/handle_title_form', methods=['POST'])
def find_recipe_by_title():
    '''Route to handle the search by title form submission.
    Arguments:
        None
    Returns:
        Redirects to the display_recipe route if the recipe is found, otherwise redirects to the 
        search_by_title route with the last search.
    '''
    searched_title = request.form.get('recipe_title')
    recipe_data = DataSource()
    recipes = recipe_data.get_recipe_by_title(searched_title)

    if not recipes:
        return search_by_title(last_search=searched_title)

    if only_one_recipe(recipes):
        return redirect(url_for('display_recipe', recipe_id=recipes[0].get_id()))

    return render_template('all_recipes.html', sorted_recipes=sort_recipes_alphabetically(recipes),
                               letters=string.ascii_uppercase, highlight=None)

def only_one_recipe(recipes):
    '''This function checks if there is only one recipe in the list.'''
    if len(recipes) == 1:
        return True
    return False


@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    '''Route to display the recipe details using display_recipe.html
    Arguments:
        recipe_id: The ID of the recipe to be displayed.
    Returns:
        Renders the display recipe template with the recipe details.
    '''
    recipe_data = DataSource()
    recipe = recipe_data.get_recipe_by_id(recipe_id)
    if recipe:
        return render_template('display_recipe.html',
                               recipe_title=recipe.get_title(),
                               recipe_ingredients=recipe.get_ingredients(),
                               recipe_instructions=recipe.get_instructions())

    return render_template('recipe_not_found_error.html')

@app.route('/autocomplete')
def autocomplete():
    '''Route to handle the autocomplete functionality for recipe titles.
    Arguments:
        None
    Returns:
        Returns a JSON response with the list of suggestions based on the query parameter.
    '''
    query = request.args.get('cur_search')
    recipe_data = DataSource()
    autocomplete_data = recipe_data.get_all_recipe_titles()
    if query:
        suggestions = [recipe for recipe in autocomplete_data if query.lower() in recipe.lower()]
        return jsonify(suggestions)
    return jsonify([])

@app.errorhandler(404)
def page_not_found(e):
    '''This function handles 404 errors with helpful usage suggestions.'''
    return render_template('404.html', error=e), 404

@app.errorhandler(500)
def python_bug(e):
    '''This function handles 500 errors, which are internal server errors.'''
    return f"A bug! {str(e)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port = 5157)
