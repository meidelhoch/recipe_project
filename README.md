# CS257-F23-TeamTemplate
Template for long-term team projects
Team E: Marc, Willan, Allison, Anika 

**Command Line Usage Statments:**  

_Search for a recipe using include/omit filters_  
\<ingredients> should be a comma-separated list of ingredients enclosed in quotes  
Usage: python cl.py --search --include_ingredients \<ingredients> --omit_ingredients \<ingredients>  
Example: python cl.py --search --include_ingredients "chicken, rice" --omit_ingredients "onion, garlic"  
Alias: --search or -s  

_Get a random recipe by specifying how many to return_  
Usage: python cl.py --random \<number>  
Example: python cl.py --random 5  
Alias: --random or -r


_Get usage information/help_  
Usage: python cl.py --help or -h  
Alias: --help or --h  
Example: python cl.py --help  

**Old Flask Usage Statements:**

_Search for a recipe using include/omit filters_  
Usage: URL/search/include/\<str:include_ingredients>/omit/\<str:omit_ingredients>  
Example: /search/include/ingredient1,ingredient2/omit/ingredient3  

_Get a random recipe by specifying how many to return_  
Usage: URL/random/\<int:number>  
Example: URL/random/3  

The main form of navigation is a nav bar that you can use to go to the different pages where the user can interact with different inputs to search by title, ingredient, randomly or look at all of the recipes

**Updated Flask Usage Statements:**    

_Homepage_: Access the main page at /.  
_Random Recipes_: Go to /random to search for a specific number of random recipes.  
_Ingredient Search_: Visit /ingredient_search to find recipes by ingredients.  
_All Recipes_: See all recipes at /all_recipes.  
_Search by Title_: Use /search_by_title to look up recipes by their names.  
_Individual Recipe_: View a recipe's details by navigating to /display_recipe/<recipe_id>, replacing <recipe_id> with the actual recipe's ID.  

## Scanability
- There is a large title the is consistent for each page and then a smaller header for each page
- The nav bar allows users to scan the things you can do with the website
- There is also a description of what you can do and where to navigate to on the home page
## Satisficing
- The navigation bar is large and at the top of the page where the user can find something similar to what they
are looking for
- There are labels on the input to tell the user to put a number and a generate button right next to it
## Muddling through
- The navigation bar stays with you on every page which allows the user to backtrack if they went somewhere they did not want to
- Buttons are intuitive with single word pages on the nav bar
- Inputs are labeled and clear what you are supposed to do

**Code Design Improvements**

## Improvement 1: 
- The Code Smell was that functions should only do 1 thing but our random() function was handling both rendering the html page for the user to enter how many random recipes they want and handling getting the results of the form. 
- Our refactored code is in app.py lines 37-73 which includes the creation of helper functions as well to shorten some of the functions in our code.
- To refactor our code we created two functions, random() and handle_random_form(). The random function only deals with rendering the html for the webpage while the handle_random_form only deals with getting the number entered by the user and finding the random recipes. This way each function has a singular focus which is either rendering html or dealing with form submission.

## Improvement 2: 
- The Code Smell was that we should encapsulate conditionals and we originally had an if statement that was: if num < 1 or num > TOTAL_NUM_RECIPES. We also earlier were checking to make sure that num is an int. So all of this code in the conditional could make it harder to read and understand our code.
- Our refactored code is in app.py lines 53 and 66-73 which is where we put in the encapsulated conditional as well as the new function that is used in place of the conditional.
- To refactor our code we created a function called is_valid_number(num) which returns True if num is actually a number and is between 1 and the number of recipes in our dataset. Then, in our code we replaced the conditional with our function and then only cast the value to an int if we had first confirmed that it was a valid number. 

## Improvement 3: 
- The Code Smell was a long method since our original get_recipe_by_ingredients function was almost 30 lines long and also sort of a code smell that functions should only do one thing but our function was building a complex SQL string and also executing the query. 
- Our refactored code is in datasource.py lines 41-71 which includes the creation of a helper function and making some of the logic more concise.
- To refactor our code we created a helper function to generate the SQL query based on the ingredients that the user wants to include and not include. This means that the get_recipe_by_ingredients function just has to call the helper function which dynamically builds a SQL query and then get_recipe_by_ingredients executes the query and returns the recipes that match. 

## Improvement 4:
- The code design pattern that we improved was adding a Singleton class and separating all our classes into different files. The new Singleton class will look at DataSource everey time a new data source class is created and if one already exists then it will use the old one and update its values, but if one does not exist then it will create a new one and add it to the stored list of all DataSource classes. The separation of all our classes into new files makes the code more neat and maintains a good level of abstracition. 
- The Singleton class will appear in datasource_meta.py and will be used in datasource.py. 
- To refactor our code we made a parent class in this new file with a call method before the constructor that checks if there is a datasource object with the same id and if there is then it returns that and if not then it makes a new one. Additionally, one new file that contains a class that was not in its own file before is recipe.py which contains the recipe class that stores recipe data. This will be used by app.py, cl.py, and the other files that use the recipe objects. 


**Front End Design Improvements**

## Improvement 1:
- When conducting usability testing, some users struggled to figure out how to use the search by ingredients functionality (ingredient_search.html). Some users would not press enter after typing in the ingredient and then submit the search which would output the no_recipes_found.html page. 
- We made the change on ingredient_search.html and no_recipes_found.html
- To fix the usability issue, we included in the search bar text a clearer prompt for the user to "press Enter after each ingredient", guiding the user better on how to properly use the functionality. We also added a note on the no_recipes_found.html page reminding the user that they might not have pressed enter after each ingredient.

## Improvement 2:
- The original recipe not found page (no_recipes_found.html) provided a generic error message when no recipes matched the users custom search critera, and the all_recipes.html results page only showed what recipes matched the criteria; however, it didn't remind users what ingredients they actually searched for. This was a usability issue because users couldn't verify what ingredients they had included or excluded. This increased cognitive load because users had to remember what they had searched, and couldn't check if they had spelled something wrong for example.
- We made the change on no_recipes_found.html and on all_recipes.html.
- To fix the usability issue, we updated both the no_recipes_found.html and the all_recipes.html to display the included and excluded ingredients that the user searched for so that the user can be reminded of the search criteria that the results are for.

## Improvement 3: 
- The original search by title (search_by_title.html) only returned a recipe if an exact match was found. So searching "Slow-Cooker Spinach Lasagna Rollups" will take you directly to that recipe, but searching "lasagna" would just return a message that says "lasagna does not exist in our database". This could be confusing to users because clearly we have lots of recipes for lasagna which they see in the autocomplete. 
- We made the change on search_by_title.html and in find_recipe_by_title() in app.py and get_recipe_by_title() in datasource.py
- To fix the usability issue, we changed it so that if a recipe matches the title searched for exactly, you get taken directly to that recipe (display_recipe.html). However, if you search for something that exists in the title of a recipe but does not match it exactly, you get taken to a page that displays all of the recipes that contain that search term in the title (all_recipes.html). If you search for something that does not appear in the title of any recipe in our database you still get a message that it does not exist. This way the user can search for both exact recipes and recipes that have a more general search term.
