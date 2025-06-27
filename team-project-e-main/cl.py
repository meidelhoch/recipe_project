'''
This file is the command line interface for the project.
'''
import sys
import argparse
from ProductionCode.datasource import DataSource


def main():
    ''' Main function to handle command line arguments and execute the appropriate function. '''
    parser = argparse.ArgumentParser(description="Recipe Search CLI")

    mode_group = parser.add_mutually_exclusive_group(required=True)

    mode_group.add_argument(
        '-s', '--search',
        action='store_true',
        help='Activate search mode based on ingredients.'
    )
    mode_group.add_argument(
        '-r', '--random',
        type=int,
        metavar='n',
        help='Select n random recipes.'
    )

    parser.add_argument(
        '-i', '--include_ingredients',
        type=str,
        default="",
        metavar='"ingredient1, ingredient2,..."',
        help='Comma-separated list of ingredients the recipe MUST ' \
        'include (use quotes). Only used with --search.'
    )
    parser.add_argument(
        '-o', '--omit_ingredients',
        type=str,
        default="",
        metavar='"ingredient3, ingredient4,..."',
        help='Comma-separated list of ingredients the recipe ' \
        'MUST NOT include (use quotes). Only used with --search.'
    )

    args = parser.parse_args()

    if (args.include_ingredients or args.omit_ingredients) and not args.search:
        parser.error('--include_ingredients and --omit_ingredients ' \
        'arguments require the --search flag.')

    include_list = []
    omit_list = []
    if args.search:
        include_list = parse_ingredients(args.include_ingredients)
        omit_list = parse_ingredients(args.omit_ingredients)
        if not include_list and not omit_list:
            print("Info: --search mode activated but no ingredients " \
            "specified via --include_ingredients or --omit_ingredients.")
        else:
            print("Searching for recipes...")
            search_cl(include_list, omit_list)
    elif args.random:
        if args.random < 1:
            print("Error: The number of random recipes must be at least 1.")
            sys.exit(1)
        print("Getting random recipes...")
        random_cl(args.random)


def search_cl(include_ingredients, omit_ingredients):
    ''' Search for recipes based on the given ingredients. '''
    ds = DataSource()
    recipes = ds.get_recipe_by_ingredients(include_ingredients, omit_ingredients)
    print_recipes(recipes)
    return recipes

def print_recipes(recipes):
    ''' Print the recipes found line by line. '''
    for recipe in recipes:
        print("Recipe Title:", recipe.get_title())
        print("Recipe Instructions:", recipe.get_instructions())
        print("Recipe Ingredients:", recipe.get_ingredients())
        print("-" * 40)

def parse_ingredients(ingredients_str):
    """
    Helper function to parse a comma-separated string of ingredients
    into a list of cleaned strings.
    """
    if ingredients_str:
        return [item.strip() for item in ingredients_str.split(',') if item.strip()]
    return []

def random_cl(num_recipes):
    ''' Get a random n number of recipes.'''
    ds = DataSource()
    random_recipes = ds.get_random_recipes(num_recipes)
    print_recipes(random_recipes)
    return random_recipes

if __name__ == "__main__":
    main()
