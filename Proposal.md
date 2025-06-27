# Title

Flavor Finder: An online recipe generator.

# Dataset(s) summary

The dataset we are going to use in this project is scraped from an online recipe website and contained a name, instructions, raw ingredients, cleaned ingredients, and image titles corresponding to a folder of images for over ten thousand recipes. The data is initially in a CSV format and we removed the columns for images and uncleaned ingredients in order to shrink the size of the dataset. In our project we will be using just the name, instructions and cleaned ingredients for our website. 

# Dataset(s) Metadata

**URL:** 

https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images?resource=download

**Date downloaded:**

4/9/2025

**Authorship:**

Sakshi Goel (Owner), Amogh Desai (Editor), Tanvi (Editor)

**Exact name and version:**

Food Ingredients and Recipes Dataset with Images (Version 1.0)

**Time period, geography, and/or scope covered:**

This dataset contains recipes from all over the world. It was all scraped from the Epicurious website at once in 2021 (couldn't find exact date but says last updated 4 years ago). 

**Location of dataset overview information:**

https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images?resource=download
All of the overview information we have is contained on the kaggle overview page.

**Location of technical documentation:**

https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images?resource=download
All of the technical documentation we have is contained on the kaggle overview page.

**Data formats:**

The data is in a CSV format and the title and instructions columns are strings and the ingrdients column is an array.

**Terms of use:**

CC BY-SA 3.0 

**Suggested citation:** 

None given but we will use the following: 

Goel, Sakshi. “Food Ingredients and Recipes Dataset with Images.” Edited by Amogh Desai and Tanvi, Kaggle, 19 Feb. 2021, www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images?resource=download. 

# Potential User Interactions

**User Story 1:** As a user, I want to find recipes to make that use of the existing ingredients in my kitchen cabinet.

**Acceptance criteria:**
- The search function should return a list of recipes that include all of the recipes that include the inputted ingredients
- The search function should return everything that contains those ingredients in alphabetical order
- The returned search results link to separate pages that contain the full recipe

**User Story 2:** As a user, I am interested in learning new interesting recipes with ingredients I already have, but also omit ingredients that I am intolerant of (due to personal preference, allergies, etc.) 

**Acceptance criteria:**
- The user can input a list of ingredients they have on hand and specify ingredients they wish to exclude (allergies/ disliked items) 
- The search function should identify recipes that contains the problematic ingredients and omits them 
- The returned results link to separate pages that contains the “safe” recipes 
- The recipes returned are tailored to dietary preferences (e.g., vegan, gluten free, etc.) 

**User Story 3:** As a user, I am looking for inspiration on what ingredients go well together in order to create my own dish.

**Acceptance criteria:**
- The user inputs a main ingredient and can browse through the recipes looking for those with similar ingredients
- The user should be able to navigate to see all possible recipes with the inputted ingredients
- For example, a user looking to cook with Chicken may look at recipes for inspiration before grocery shopping for ingredients (example: tomatoes goes well with eggs) 

**User Story 4:** As a user, I am not sure what I want to eat and am looking for interesting recipes to try out.

**Acceptance criteria:**
- The system outputs 5 random recipes.
- If the user is not satisfied with the results, they can regenerate the search to find 5 more random recipes.
- The returned search results link to separate pages that contain the full recipe