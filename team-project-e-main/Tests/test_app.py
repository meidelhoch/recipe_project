'''Tests for Flask application routes.'''
import unittest
from unittest.mock import MagicMock, patch
from app import app
from ProductionCode.datasource import DataSource

# WE SHOULD ALSO HAVE TESTS THAT ACTUALLY TEST DATASOURCE

class TestFlaskRoutes(unittest.TestCase):
    '''Test case for Flask application routes.'''

    @patch('ProductionCode.datasource.psycopg2.connect')
    def setUp(self, mock_connect):
        self.app = app.test_client()
        # create a mock connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.ds = DataSource()

    def test_homepage(self):
        '''Test the homepage route.'''
        self.ds.cursor.fetchone.return_value = (789,
            'Cavatappi with Broccolini, Brown Butter, and Sage',
             'Bring a large pot of water to a boil. Fill a large bowl with water and ice '
             'and set aside.\nAdd 1 tablespoon kosher salt and the broccolini to the '
             'boiling water and cook until crisp-tender, 2 to 3 minutes. Using a spider '
             'or slotted spoon, transfer the Broccolini to the ice water to stop the '
             'cooking and let cool. Keep the pot of water boiling for the pasta. Drain '
             'the broccolini in a colander, cut the stalks in half crosswise, and set '
             'aside.\nIn a large nonstick skillet over medium heat, heat the olive oil '
             'until shimmering. Add the garlic and red pepper flakes and cook, stirring '
             'frequently, for 1 minute. Add the blanched broccolini, 1/2 teaspoon salt, '
             'and 1/4 teaspoon black pepper and sauté until tender, 3 to 5 minutes. '
             'Transfer the broccolini to a medium bowl and set aside.\nAdd the pasta '
             'to the boiling water and cook until al dente, about 2 minutes less than the '
             'directions on the package. Reserve 1/2 cup of the pasta water and drain the '
             'pasta in a colander.\nMeanwhile, wipe out the skillet, return it to '
             'medium-low heat, and add the butter. When the butter has melted, add the sage '
             'leaves and cook until the butter turns amber brown and the sage shrivels, 4 '
             'to 6 minutes. Add 1/4 teaspoon salt and black pepper. Stir in the cooked pasta '
             'until incorporated, then fold in the broccolini and 2 to 3 tablespoons of the '
             'reserved pasta water.\nStir in the Parmesan cheese, adding more pasta water until '
             'you achieve desired creaminess. Season with salt and pepper and serve hot.',
             "['Kosher salt', '2 bunches Broccolini (about 1 pound), ends trimmed, split "
             "lengthwise into halves or thirds depending on the thickness (or substitute "
             "broccoli rabe or broccoli)', '2 tablespoons extra-virgin olive oil', '2 large cloves "
             "garlic, minced', '1/4 teaspoon crushed red pepper flakes', 'Freshly ground black "
             "pepper', '1 pound cavatappi pasta (or your favorite ribbed pasta)', '6 tablespoons "
             "unsalted butter, cubed', '15 fresh sage leaves, torn', '1/2 cup freshly grated "
             "Parmesan cheese']")
        self.ds.cursor.fetchall.return_value = [
            (789, 'Cavatappi with Broccolini, Brown Butter, and Sage',
             'Bring a large pot of water to a boil. Fill a large bowl with water and ice '
             'and set aside.\nAdd 1 tablespoon kosher salt and the broccolini to the '
             'boiling water and cook until crisp-tender, 2 to 3 minutes. Using a spider '
             'or slotted spoon, transfer the Broccolini to the ice water to stop the '
             'cooking and let cool. Keep the pot of water boiling for the pasta. Drain '
             'the broccolini in a colander, cut the stalks in half crosswise, and set '
             'aside.\nIn a large nonstick skillet over medium heat, heat the olive oil '
             'until shimmering. Add the garlic and red pepper flakes and cook, stirring '
             'frequently, for 1 minute. Add the blanched broccolini, 1/2 teaspoon salt, '
             'and 1/4 teaspoon black pepper and sauté until tender, 3 to 5 minutes. '
             'Transfer the broccolini to a medium bowl and set aside.\nAdd the pasta '
             'to the boiling water and cook until al dente, about 2 minutes less than the '
             'directions on the package. Reserve 1/2 cup of the pasta water and drain the '
             'pasta in a colander.\nMeanwhile, wipe out the skillet, return it to '
             'medium-low heat, and add the butter. When the butter has melted, add the sage '
             'leaves and cook until the butter turns amber brown and the sage shrivels, 4 '
             'to 6 minutes. Add 1/4 teaspoon salt and black pepper. Stir in the cooked pasta '
             'until incorporated, then fold in the broccolini and 2 to 3 tablespoons of the '
             'reserved pasta water.\nStir in the Parmesan cheese, adding more pasta water until '
             'you achieve desired creaminess. Season with salt and pepper and serve hot.',
             "['Kosher salt', '2 bunches Broccolini (about 1 pound), ends trimmed, split "
             "lengthwise into halves or thirds depending on the thickness (or substitute "
             "broccoli rabe or broccoli)', '2 tablespoons extra-virgin olive oil', '2 large cloves "
             "garlic, minced', '1/4 teaspoon crushed red pepper flakes', 'Freshly ground black "
             "pepper', '1 pound cavatappi pasta (or your favorite ribbed pasta)', '6 tablespoons "
             "unsalted butter, cubed', '15 fresh sage leaves, torn', '1/2 cup freshly grated "
             "Parmesan cheese']"),
            (944, 'Charred Steak and Broccolini with Cheese Sauce',
             'Preheat oven to 450°F. Season steaks all over with pepper and 1 1/2 tsp. kosher '
             'salt. Let sit 10 minutes.\nMeanwhile, toss broccolini, oil, and 1/2 tsp. kosher '
             'salt on a rimmed baking sheet to combine. Spread out in a single layer and set '
             'aside.\nUsing tongs if needed, hold both steaks together fat cap side down in a '
             'large ovenproof skillet, then set over high heat. Cook until pan is coated in fat, '
             'about 4 minutes. Lay steaks flat and continue to sear until deeply browned, about '
             '3 minutes per side. Transfer skillet to oven and roast steaks until an instant-read '
             'thermometer inserted into the thickest part registers 120°F for medium-rare, 6–8 '
             'minutes. Transfer to a cutting board and let rest 10 minutes before slicing.\nWhile '
             'steaks are resting, roast reserved broccolini until crisp-tender and lightly '
             'charred, about 10 minutes.\nHeat cheese, cream cheese, milk, nutmeg, cayenne, and '
             'remaining 1/4 tsp. kosher salt in a medium saucepan over medium, whisking '
             'constantly, until a smooth sauce forms, about 5 minutes.\nDivide sauce among '
             'plates. Top with broccolini and steaks; sprinkle with sea salt.',
             '[\'2 (1 1/2"–2" thick) boneless New York strip steaks\', \'1 tsp. freshly ground '
             'black pepper\', \'2 1/4 tsp. kosher salt, divided\', \'2 bunches broccolini '
             '(about 1 lb. total), trimmed, halved lengthwise\', \'1 Tbsp. extra-virgin olive '
             'oil\', \'3 oz. coarsely grated Gruyère (about 1½ cups)\', \'3 oz. cream cheese, '
             'cut into pieces\', \'3/4 cup whole milk\', \'1/4 tsp. freshly grated or ground '
             'nutmeg\', \'Large pinch of cayenne pepper\', \'Flaky sea salt\']'),
            (11286, 'Chocolate and Peppermint Candy Ice Cream Sandwiches', 'Stir together '
            'ice cream (reserve pint container), '
             'extract, and 1/2 cup crushed candy in a bowl until combined.\nTransfer mixture '
             'to pint container and freeze until just firm enough to scoop, about 1 hour.\n '
             'Working very quickly, scoop ice cream onto flat sides of 8 wafers (1 scoop per '
             'wafer), then top with remaining 8 wafers, flat sides down. Wrap each sandwich '
             'individually with plastic wrap and freeze until firm, about 1 hour. Unwrap '
             'sandwiches and roll edges in remaining 1/2 cup crushed candy. Rewrap and freeze '
             'until firm, about 1 hour.', 
             "['1 pint superpremium vanilla ice cream, softened "
             "slightly', '1/4 teaspoon pure peppermint extract', '1 cup finely crushed peppermint "
             "hard candies (1/4 lb)', '16 chocolate wafers such as Nabisco Famous', 'a 1/4-cup "
             "ice cream scoop']")]
        response = self.app.get('/')
        self.assertIn(b"This website allows users to find random recipes, or " \
        b"to search for recipes by title or by ingredients. This way anybody " \
        b"can find a delicious recipe to fit any situation.",
                      response.data, "Should match")

    def test_all_recipes(self):
        '''Test the all recipes route.'''
        self.ds.cursor.fetchall.return_value = [
            (789, 'Cavatappi with Broccolini, Brown Butter, and Sage',
             'Bring a large pot of water to a boil. Fill a large bowl with water and ice '
             'and set aside.\nAdd 1 tablespoon kosher salt and the broccolini to the '
             'boiling water and cook until crisp-tender, 2 to 3 minutes. Using a spider '
             'or slotted spoon, transfer the Broccolini to the ice water to stop the '
             'cooking and let cool. Keep the pot of water boiling for the pasta. Drain '
             'the broccolini in a colander, cut the stalks in half crosswise, and set '
             'aside.\nIn a large nonstick skillet over medium heat, heat the olive oil '
             'until shimmering. Add the garlic and red pepper flakes and cook, stirring '
             'frequently, for 1 minute. Add the blanched broccolini, 1/2 teaspoon salt, '
             'and 1/4 teaspoon black pepper and sauté until tender, 3 to 5 minutes. '
             'Transfer the broccolini to a medium bowl and set aside.\nAdd the pasta '
             'to the boiling water and cook until al dente, about 2 minutes less than the '
             'directions on the package. Reserve 1/2 cup of the pasta water and drain the '
             'pasta in a colander.\nMeanwhile, wipe out the skillet, return it to '
             'medium-low heat, and add the butter. When the butter has melted, add the sage '
             'leaves and cook until the butter turns amber brown and the sage shrivels, 4 '
             'to 6 minutes. Add 1/4 teaspoon salt and black pepper. Stir in the cooked pasta '
             'until incorporated, then fold in the broccolini and 2 to 3 tablespoons of the '
             'reserved pasta water.\nStir in the Parmesan cheese, adding more pasta water until '
             'you achieve desired creaminess. Season with salt and pepper and serve hot.',
             "['Kosher salt', '2 bunches Broccolini (about 1 pound), ends trimmed, split "
             "lengthwise into halves or thirds depending on the thickness (or substitute "
             "broccoli rabe or broccoli)', '2 tablespoons extra-virgin olive oil', '2 large cloves "
             "garlic, minced', '1/4 teaspoon crushed red pepper flakes', 'Freshly ground black "
             "pepper', '1 pound cavatappi pasta (or your favorite ribbed pasta)', '6 tablespoons "
             "unsalted butter, cubed', '15 fresh sage leaves, torn', '1/2 cup freshly grated "
             "Parmesan cheese']"),
            (944, 'Charred Steak and Broccolini with Cheese Sauce',
             'Preheat oven to 450°F. Season steaks all over with pepper and 1 1/2 tsp. kosher '
             'salt. Let sit 10 minutes.\nMeanwhile, toss broccolini, oil, and 1/2 tsp. kosher '
             'salt on a rimmed baking sheet to combine. Spread out in a single layer and set '
             'aside.\nUsing tongs if needed, hold both steaks together fat cap side down in a '
             'large ovenproof skillet, then set over high heat. Cook until pan is coated in fat, '
             'about 4 minutes. Lay steaks flat and continue to sear until deeply browned, about '
             '3 minutes per side. Transfer skillet to oven and roast steaks until an instant-read '
             'thermometer inserted into the thickest part registers 120°F for medium-rare, 6–8 '
             'minutes. Transfer to a cutting board and let rest 10 minutes before slicing.\nWhile '
             'steaks are resting, roast reserved broccolini until crisp-tender and lightly '
             'charred, about 10 minutes.\nHeat cheese, cream cheese, milk, nutmeg, cayenne, and '
             'remaining 1/4 tsp. kosher salt in a medium saucepan over medium, whisking '
             'constantly, until a smooth sauce forms, about 5 minutes.\nDivide sauce among '
             'plates. Top with broccolini and steaks; sprinkle with sea salt.',
             '[\'2 (1 1/2"–2" thick) boneless New York strip steaks\', \'1 tsp. freshly ground '
             'black pepper\', \'2 1/4 tsp. kosher salt, divided\', \'2 bunches broccolini '
             '(about 1 lb. total), trimmed, halved lengthwise\', \'1 Tbsp. extra-virgin olive '
             'oil\', \'3 oz. coarsely grated Gruyère (about 1½ cups)\', \'3 oz. cream cheese, '
             'cut into pieces\', \'3/4 cup whole milk\', \'1/4 tsp. freshly grated or ground '
             'nutmeg\', \'Large pinch of cayenne pepper\', \'Flaky sea salt\']'),
            (11286, 'Chocolate and Peppermint Candy Ice Cream Sandwiches', 'Stir together '
            'ice cream (reserve pint container), '
             'extract, and 1/2 cup crushed candy in a bowl until combined.\nTransfer mixture '
             'to pint container and freeze until just firm enough to scoop, about 1 hour.\n '
             'Working very quickly, scoop ice cream onto flat sides of 8 wafers (1 scoop per '
             'wafer), then top with remaining 8 wafers, flat sides down. Wrap each sandwich '
             'individually with plastic wrap and freeze until firm, about 1 hour. Unwrap '
             'sandwiches and roll edges in remaining 1/2 cup crushed candy. Rewrap and freeze '
             'until firm, about 1 hour.', 
             "['1 pint superpremium vanilla ice cream, softened "
             "slightly', '1/4 teaspoon pure peppermint extract', '1 cup finely crushed peppermint "
             "hard candies (1/4 lb)', '16 chocolate wafers such as Nabisco Famous', 'a 1/4-cup "
             "ice cream scoop']")]
        response = self.app.get('/all_recipes')
        self.assertIn(b"Charred Steak and Broccolini", response.data, "Should match")

    def test_random_route(self):
        '''Test the random route.'''
        self.ds.cursor.fetchall.return_value = [
            (11286, 'Chocolate and Peppermint Candy Ice Cream Sandwiches',
             'Stir together ice cream (reserve pint container), extract, and 1/2 cup crushed '
             'candy in a bowl until combined.\nTransfer mixture to pint container and freeze '
             'until just firm enough to scoop, about 1 hour.\n Working very quickly, scoop '
             'ice cream onto flat sides of 8 wafers (1 scoop per wafer), then top with '
             'remaining 8 wafers, flat sides down. Wrap each sandwich individually with '
             'plastic wrap and freeze until firm, about 1 hour. Unwrap sandwiches and roll '
             'edges in remaining 1/2 cup crushed candy. Rewrap and freeze until firm, about 1 '
             'hour.', 
             "['1 pint superpremium vanilla ice cream, softened slightly', '1/4 teaspoon pure "
             "peppermint extract', '1 cup finely crushed peppermint hard candies (1/4 lb)', "
             "'16 chocolate wafers such as Nabisco Famous', 'a 1/4-cup ice cream scoop']")]
        # Mock the form submission for the random route
        response = self.app.post('/handle_random_form', data={'num_recipes': '1'})

        self.assertIn(b"Chocolate and Peppermint Candy Ice Cream Sandwiches",
                      response.data, "Should match")

    def test_search_by_title_route(self):
        '''Test the random route.'''
        self.ds.cursor.fetchone.return_value = (11286,
            'Chocolate and Peppermint Candy Ice Cream Sandwiches',
             'Stir together ice cream (reserve pint container), extract, and 1/2 cup crushed '
             'candy in a bowl until combined.\nTransfer mixture to pint container and freeze '
             'until just firm enough to scoop, about 1 hour.\n Working very quickly, scoop '
             'ice cream onto flat sides of 8 wafers (1 scoop per wafer), then top with '
             'remaining 8 wafers, flat sides down. Wrap each sandwich individually with '
             'plastic wrap and freeze until firm, about 1 hour. Unwrap sandwiches and roll '
             'edges in remaining 1/2 cup crushed candy. Rewrap and freeze until firm, about 1 '
             'hour.', 
             "['1 pint superpremium vanilla ice cream, softened slightly', '1/4 teaspoon pure "
             "peppermint extract', '1 cup finely crushed peppermint hard candies (1/4 lb)', "
             "'16 chocolate wafers such as Nabisco Famous', 'a 1/4-cup ice cream scoop']")
        # Mock the form submission for the random route
        response = self.app.post('/handle_title_form',
                                 data={'recipe_title':
                                       "Chocolate and Peppermint Candy Ice Cream Sandwiches"},
                                 follow_redirects=True)

        self.assertIn(b"Chocolate and Peppermint Candy Ice Cream Sandwiches",
                      response.data, "Should match")

    def test_search_by_title_no_match(self):
        '''Test the search by title route with no perfect match.'''
        self.ds.cursor.fetchone.return_value = None
        self.ds.cursor.fetchall.return_value = [
            (789, 'Cavatappi with Broccolini, Brown Butter, and Sage',
             'Bring a large pot of water to a boil. Fill a large bowl with water and ice '
             'and set aside.\nAdd 1 tablespoon kosher salt and the broccolini to the '
             'boiling water and cook until crisp-tender, 2 to 3 minutes. Using a spider '
             'or slotted spoon, transfer the Broccolini to the ice water to stop the '
             'cooking and let cool. Keep the pot of water boiling for the pasta. Drain '
             'the broccolini in a colander, cut the stalks in half crosswise, and set '
             'aside.\nIn a large nonstick skillet over medium heat, heat the olive oil '
             'until shimmering. Add the garlic and red pepper flakes and cook, stirring '
             'frequently, for 1 minute. Add the blanched broccolini, 1/2 teaspoon salt, '
             'and 1/4 teaspoon black pepper and sauté until tender, 3 to 5 minutes. '
             'Transfer the broccolini to a medium bowl and set aside.\nAdd the pasta '
             'to the boiling water and cook until al dente, about 2 minutes less than the '
             'directions on the package. Reserve 1/2 cup of the pasta water and drain the '
             'pasta in a colander.\nMeanwhile, wipe out the skillet, return it to '
             'medium-low heat, and add the butter. When the butter has melted, add the sage '
             'leaves and cook until the butter turns amber brown and the sage shrivels, 4 '
             'to 6 minutes. Add 1/4 teaspoon salt and black pepper. Stir in the cooked pasta '
             'until incorporated, then fold in the broccolini and 2 to 3 tablespoons of the '
             'reserved pasta water.\nStir in the Parmesan cheese, adding more pasta water until '
             'you achieve desired creaminess. Season with salt and pepper and serve hot.',
             "['Kosher salt', '2 bunches Broccolini (about 1 pound), ends trimmed, split "
             "lengthwise into halves or thirds depending on the thickness (or substitute "
             "broccoli rabe or broccoli)', '2 tablespoons extra-virgin olive oil', '2 large cloves "
             "garlic, minced', '1/4 teaspoon crushed red pepper flakes', 'Freshly ground black "
             "pepper', '1 pound cavatappi pasta (or your favorite ribbed pasta)', '6 tablespoons "
             "unsalted butter, cubed', '15 fresh sage leaves, torn', '1/2 cup freshly grated "
             "Parmesan cheese']"),
            (944, 'Charred Steak and Broccolini with Cheese Sauce',
             'Preheat oven to 450°F. Season steaks all over with pepper and 1 1/2 tsp. kosher '
             'salt. Let sit 10 minutes.\nMeanwhile, toss broccolini, oil, and 1/2 tsp. kosher '
             'salt on a rimmed baking sheet to combine. Spread out in a single layer and set '
             'aside.\nUsing tongs if needed, hold both steaks together fat cap side down in a '
             'large ovenproof skillet, then set over high heat. Cook until pan is coated in fat, '
             'about 4 minutes. Lay steaks flat and continue to sear until deeply browned, about '
             '3 minutes per side. Transfer skillet to oven and roast steaks until an instant-read '
             'thermometer inserted into the thickest part registers 120°F for medium-rare, 6–8 '
             'minutes. Transfer to a cutting board and let rest 10 minutes before slicing.\nWhile '
             'steaks are resting, roast reserved broccolini until crisp-tender and lightly '
             'charred, about 10 minutes.\nHeat cheese, cream cheese, milk, nutmeg, cayenne, and '
             'remaining 1/4 tsp. kosher salt in a medium saucepan over medium, whisking '
             'constantly, until a smooth sauce forms, about 5 minutes.\nDivide sauce among '
             'plates. Top with broccolini and steaks; sprinkle with sea salt.',
             '[\'2 (1 1/2"–2" thick) boneless New York strip steaks\', \'1 tsp. freshly ground '
             'black pepper\', \'2 1/4 tsp. kosher salt, divided\', \'2 bunches broccolini '
             '(about 1 lb. total), trimmed, halved lengthwise\', \'1 Tbsp. extra-virgin olive '
             'oil\', \'3 oz. coarsely grated Gruyère (about 1½ cups)\', \'3 oz. cream cheese, '
             'cut into pieces\', \'3/4 cup whole milk\', \'1/4 tsp. freshly grated or ground '
             'nutmeg\', \'Large pinch of cayenne pepper\', \'Flaky sea salt\']'),
            (11286, 'Chocolate and Peppermint Candy Ice Cream Sandwiches', 'Stir together '
            'ice cream (reserve pint container), '
             'extract, and 1/2 cup crushed candy in a bowl until combined.\nTransfer mixture '
             'to pint container and freeze until just firm enough to scoop, about 1 hour.\n '
             'Working very quickly, scoop ice cream onto flat sides of 8 wafers (1 scoop per '
             'wafer), then top with remaining 8 wafers, flat sides down. Wrap each sandwich '
             'individually with plastic wrap and freeze until firm, about 1 hour. Unwrap '
             'sandwiches and roll edges in remaining 1/2 cup crushed candy. Rewrap and freeze '
             'until firm, about 1 hour.', 
             "['1 pint superpremium vanilla ice cream, softened "
             "slightly', '1/4 teaspoon pure peppermint extract', '1 cup finely crushed peppermint "
             "hard candies (1/4 lb)', '16 chocolate wafers such as Nabisco Famous', 'a 1/4-cup "
             "ice cream scoop']")]
        response = self.app.post('/handle_title_form',
                                 data={'recipe_title': "Broccolini"},
                                 follow_redirects=True)

        self.assertIn(b"Cavatappi", response.data, "Should match")
        self.assertIn(b"Steak", response.data, "Should match")


    def test_random_route_invalid(self):
        '''Test the random route with an invalid number.'''
        self.ds.cursor.fetchall.return_value = []
        response = self.app.post('/handle_random_form', data={'num_recipes': -1})

        self.assertIn(b"You entered an invalid number of recipes",
                      response.data, "Should match")

    def test_autocomplete_route(self):
        '''Test the autocomplete route.'''
        self.ds.cursor.fetchall.return_value = [
            ("Chocolate Cake",),
            ("Chocolate Chip Cookies",),
            ("Vanilla Ice Cream",),
            ("Peppermint Bark",),
            ("Chocolate and Peppermint Candy Ice Cream Sandwiches",)
        ]


        # Query for "chocolate"
        response = self.app.get('/autocomplete?cur_search=chocolate')
        data = response.get_json()
        self.assertIn("Chocolate Cake", data)
        self.assertIn("Chocolate Chip Cookies", data)
        self.assertIn("Chocolate and Peppermint Candy Ice Cream Sandwiches", data)
        self.assertNotIn("Vanilla Ice Cream", data)

    def test_search_include_route(self):
        '''Test the search include route.'''
        self.ds.cursor.fetchall.return_value = [
            (789, 'Cavatappi with Broccolini, Brown Butter, and Sage',
             'Bring a large pot of water to a boil. Fill a large bowl with water and ice '
             'and set aside.\nAdd 1 tablespoon kosher salt and the broccolini to the '
             'boiling water and cook until crisp-tender, 2 to 3 minutes. Using a spider '
             'or slotted spoon, transfer the Broccolini to the ice water to stop the '
             'cooking and let cool. Keep the pot of water boiling for the pasta. Drain '
             'the broccolini in a colander, cut the stalks in half crosswise, and set '
             'aside.\nIn a large nonstick skillet over medium heat, heat the olive oil '
             'until shimmering. Add the garlic and red pepper flakes and cook, stirring '
             'frequently, for 1 minute. Add the blanched broccolini, 1/2 teaspoon salt, '
             'and 1/4 teaspoon black pepper and sauté until tender, 3 to 5 minutes. '
             'Transfer the broccolini to a medium bowl and set aside.\nAdd the pasta '
             'to the boiling water and cook until al dente, about 2 minutes less than the '
             'directions on the package. Reserve 1/2 cup of the pasta water and drain the '
             'pasta in a colander.\nMeanwhile, wipe out the skillet, return it to '
             'medium-low heat, and add the butter. When the butter has melted, add the sage '
             'leaves and cook until the butter turns amber brown and the sage shrivels, 4 '
             'to 6 minutes. Add 1/4 teaspoon salt and black pepper. Stir in the cooked pasta '
             'until incorporated, then fold in the broccolini and 2 to 3 tablespoons of the '
             'reserved pasta water.\nStir in the Parmesan cheese, adding more pasta water until '
             'you achieve desired creaminess. Season with salt and pepper and serve hot.',
             "['Kosher salt', '2 bunches Broccolini (about 1 pound), ends trimmed, split "
             "lengthwise into halves or thirds depending on the thickness (or substitute "
             "broccoli rabe or broccoli)', '2 tablespoons extra-virgin olive oil', '2 large cloves "
             "garlic, minced', '1/4 teaspoon crushed red pepper flakes', 'Freshly ground black "
             "pepper', '1 pound cavatappi pasta (or your favorite ribbed pasta)', '6 tablespoons "
             "unsalted butter, cubed', '15 fresh sage leaves, torn', '1/2 cup freshly grated "
             "Parmesan cheese']"),
            (944, 'Charred Steak and Broccolini with Cheese Sauce',
             'Preheat oven to 450°F. Season steaks all over with pepper and 1 1/2 tsp. kosher '
             'salt. Let sit 10 minutes.\nMeanwhile, toss broccolini, oil, and 1/2 tsp. kosher '
             'salt on a rimmed baking sheet to combine. Spread out in a single layer and set '
             'aside.\nUsing tongs if needed, hold both steaks together fat cap side down in a '
             'large ovenproof skillet, then set over high heat. Cook until pan is coated in fat, '
             'about 4 minutes. Lay steaks flat and continue to sear until deeply browned, about '
             '3 minutes per side. Transfer skillet to oven and roast steaks until an instant-read '
             'thermometer inserted into the thickest part registers 120°F for medium-rare, 6–8 '
             'minutes. Transfer to a cutting board and let rest 10 minutes before slicing.\nWhile '
             'steaks are resting, roast reserved broccolini until crisp-tender and lightly '
             'charred, about 10 minutes.\nHeat cheese, cream cheese, milk, nutmeg, cayenne, and '
             'remaining 1/4 tsp. kosher salt in a medium saucepan over medium, whisking '
             'constantly, until a smooth sauce forms, about 5 minutes.\nDivide sauce among '
             'plates. Top with broccolini and steaks; sprinkle with sea salt.',
             '[\'2 (1 1/2"–2" thick) boneless New York strip steaks\', \'1 tsp. freshly ground '
             'black pepper\', \'2 1/4 tsp. kosher salt, divided\', \'2 bunches broccolini '
             '(about 1 lb. total), trimmed, halved lengthwise\', \'1 Tbsp. extra-virgin olive '
             'oil\', \'3 oz. coarsely grated Gruyère (about 1½ cups)\', \'3 oz. cream cheese, '
             'cut into pieces\', \'3/4 cup whole milk\', \'1/4 tsp. freshly grated or ground '
             'nutmeg\', \'Large pinch of cayenne pepper\', \'Flaky sea salt\']')]
        response = self.app.post('/handle_ingredient_search',
                                 data={'include_ingredients': "cheese,broccoli",
                                        'exclude_ingredients': ""})

        self.assertIn(b"Cavatappi with Broccolini, Brown Butter, and Sage",
                      response.data, "Should match")

    def test_search_omit_route(self):
        '''Test the search omit route.'''
        self.ds.cursor.fetchall.return_value = [
            (13465,
             'Spaghetti with Anchovies, Olives, and Toasted Bread Crumbs',
             'Fill a 6-quart pasta pot three fourths full with salted water and bring to '
             'a boil for pasta.\nTear bread into pieces and in a blender or food processor '
             'pulse to make coarse crumbs. Finely chop onion. Mince garlic. Rinse anchovies '
             'and pat dry. In a sieve rinse and drain peppers and olives. Cut peppers into '
             '1‚-inch-long strips and quarter olives.\nIn a deep 12-inch heavy skillet heat '
             '2 tablespoons oil over moderate heat until hot but not smoking and stir in bread '
             'crumbs. Toast bread crumbs, stirring constantly, until golden and crisp, about 2 '
             'minutes, and transfer to a plate to cool. Wipe skillet clean.\nIn skillet heat '
             'remaining 4 tablespoons oil over moderately high heat until hot but not smoking '
             'and cook onion, stirring, until golden brown on edges. Remove skillet from heat '
             'and add garlic and anchovies. Cook mixture over moderately low heat, '
             'stirring until fillets are dissolved, about 2 minutes. Carefully pour wine down '
             'side of skillet and simmer, stirring occasionally, until liquid is reduced to '
             'about 2 tablespoons. Remove skillet from heat and stir in peppers, olives, and '
             '1/4 cup parsley.\nCook pasta in boiling water, stirring occasionally, until al '
             'dente and ladle out and reserve 1 cup pasta water. Drain pasta in a colander '
             'and add to sauce with 1/2 cup reserved pasta water and salt and pepper to taste. '
             'Heat mixture over low heat, gently tossing (and adding more pasta water as needed '
             'if mixture becomes dry), until just heated through. Sprinkle pasta with remaining '
             '1/4 cup parsley and some bread crumbs and serve remaining bread crumbs on the side.',
             "['1 pound dried spaghetti or linguine', '3 slices firm white sandwich bread', '1 "
             "onion', '3 large garlic cloves', '8 to 10 bottled or canned flat anchovy fillets', "
             "'a 12-ounce jar roasted red peppers', 'a 2 1/4-ounce jar pitted green olives (about "
             "3/4 cup)', '6 tablespoons olive oil', '1 cup dry white wine', '1/2 cup chopped "
             "fresh flat-leafed parsley leaves']"),
            (13466,
             'Salmon with Soy-Honey and Wasabi Sauces',
             'Stir together mirin, soy sauce, vinegar, and ginger in a shallow dish. Add fish, '
             'skin sides up, and marinate, covered, at room temperature 10 minutes.\nPreheat '
             'broiler.\nBoil soy sauce, honey, and lime juice in a small saucepan, stirring '
             'frequently, until thickened, about 4 minutes.\nStir together wasabi powder and '
             'water in a small bowl.\nBroil fish, skin sides down, on oiled rack of a broiler '
             'pan 5 to 7 inches from heat until fish is just cooked through, about 6 minutes.\n'
             'Serve salmon drizzled with sauces.', 
             "['1/2 cupmirin (Japanese sweet rice wine)', '2 tablespoons soy sauce', '1/4 cup "
             "rice vinegar (not seasoned)', '1 tablespoon finely grated peeled fresh ginger', "
             "'4 (6-ounce) pieces salmon fillet', '2 tablespoons soy sauce', '1/4 cup honey', "
             "'1 tablespoon fresh lime juice', '2 teaspoons wasabi powder', '1 tablespoon water', "
             "'Accompaniment: lime wedges']"),
            (13467,
             'Veal Cutlets with Arugula and Tomato Salad', 'Put oven rack in middle position '
             'and preheat oven to 350°F.\nSpread bread crumbs in a shallow baking pan and '
             'toast 8 to 10 minutes. Reduce oven temperature to 200°F.\nWhisk together oil, '
             'juice, pepper, and 1/2 teaspoon salt in a large bowl until combined, then stir '
             'in tomatoes and onion.\nGently pound cutlets to 1/8-inch thickness between 2 '
             'sheets of plastic wrap with flat side of a meat pounder or with a rolling pin. '
             'Sprinkle veal all over with remaining 1/2 teaspoon salt and season with '
             'pepper.\nStir together bread crumbs and cheese in a large shallow bowl. Lightly '
             'beat eggs in another large shallow bowl. Dip veal, 1 piece at a time, in egg, '
             'letting excess drip off, then dredge in bread crumbs, coating completely, '
             'and arrange in 1 layer on a sheet of wax paper.\nHeat 3 tablespoons vegetable '
             'oil in a 12-inch heavy skillet over moderately high heat until hot but not smoking, '
             'then fry 2 cutlets, turning over once, until golden brown and just cooked through, '
             'about 6 minutes total. Transfer to paper towels to drain briefly, then transfer to '
             'baking pan and keep warm in oven. Add remaining 3 tablespoons oil to skillet '
             'and fry remaining cutlets.\nAdd arugula and basil to tomato mixture and toss, then '
             'season with salt and pepper. 3Serve veal topped with salad.',
             "['3 cups fine fresh bread crumbs (from 6 slices firm white sandwich bread)', '6 "
             "tablespoons olive oil', '3 tablespoons fresh lemon juice', '1 teaspoon black "
             "pepper', '1 teaspoon salt', '2 medium tomatoes (1/8 lb total), cut into "
             "1/2-inch-thick wedges', '1 small red onion, halved lengthwise, then thinly "
             "sliced crosswise (1/2 cup)', '4 veal cutlets (1 1/4 lb total)', '2 oz finely "
             "grated Parmigiano-Reggiano (1 cup)', '2 large eggs', '6 tablespoons vegetable "
             "oil', '10 oz arugula (5 cups), leaves torn if large', '1 cup loosely packed "
             "fresh basil leaves', 'torn into bite-size pieces']")]
        response = self.app.post('/handle_ingredient_search', data={'include_ingredients': "",
                                                  'exclude_ingredients': "cheese,broccoli"})

        self.assertIn(b"Salmon with Soy-Honey and Wasabi Sauces",
                      response.data, "Should match")


    def test_search_include_omit_route(self):
        '''Test the search include and omit route.'''
        self.ds.cursor.fetchall.return_value = [
            (11329, 'Broccoli-Mascarpone Soup',
             'Heat oil in large pot over medium heat. Add shallots; sauté 3 minutes. Add '
             'broccoli; sauté 1 minute. Add broth; bring to boil. Reduce heat to medium-low. '
             'Cover and simmer until vegetables are tender, about 10 minutes. Cool slightly.\n'
             'Working in batches, transfer soup to blender; puree until smooth. Return to pot. '
             'Reserve 1/4 cup mascarpone in small bowl; cover and chill. Whisk 1 1/4 cups '
             'mascarpone and cayenne pepper into soup. Season with salt. DO AHEAD Can be '
             'made 1 day ahead. Cover; chill. Heat soup over medium heat, stirring occasionally; '
             'do not boil.\nLadle soup into bowls. Garnish with reserved mascarpone. Sprinkle '
             'with chopped chives and serve.',
             "['3 tablespoons olive oil', '1 1/2 cups sliced shallots (about 6 large)', '1 1/2 "
             "pounds broccoli florets, cut into 1-inch pieces', '6 cups low-salt chicken broth', "
             "'1 1/2 cups (12 ounces) mascarpone cheese (Italian cream cheese), divided', '1/4 "
             "teaspoon cayenne pepper', '3 tablespoons chopped fresh chives']"),
            (11538,
             'Mac and Cheese with Chicken and Broccoli',
             'Prepare barbecue (medium heat). Sprinkle chicken with salt and pepper. Brush both '
             'sides with olive oil. Grill until cooked through, about 6 minutes per side. Dice '
             'chicken and set aside. Cook broccoli in medium pot of boiling salted water until '
             'crisp-tender, about 3 minutes. Set aside.\nMelt butter in heavy large saucepan '
             'over medium heat. Add flour and cook 2 minutes, stirring constantly. Gradually mix '
             'in cream. Bring to boil, reduce heat, and simmer 10 minutes, stirring frequently. '
             'Add both cheeses and stir until sauce is smooth. Season to taste with salt and '
             'pepper. Add pasta, chicken, and broccoli to sauce; mix well. Garnish with chives '
             'and serve.',
             "['1 pound skinless boneless chicken breasts', 'Olive oil (for "
             "brushing)', '2 heads of broccoli, cut into florets (about 5 cups)', '2 tablespoons "
             "(1/4 stick) unsalted butter', '2 tablespoons all purpose flour', '4 cups whipping "
             "cream', '1 cup grated Fontina cheese (about 4 ounces)', '1 cup grated cheddar cheese "
             "(about 4 ounces)', '1 pound pasta shells, freshly cooked', '1/2 bunch fresh chives', "
             "'chopped']"),
            (12574,
             'Cauliflower and Broccoli Flan with Spinach Bechamel',
             'Cook cauliflower and broccoli in large pot of boiling salted water until '
             'crisp-tender, about 5 minutes. Drain, reserving 2/3 cup cooking liquid. Transfer '
             'vegetables to large bowl. Cool.\nRinse spinach, then toss in large nonstick skillet '
             'over medium-high heat until just wilted. Drain and cool. Squeeze spinach '
             'dry; finely chop.\nMelt butter in heavy medium saucepan over medium heat. Add flour '
             'and whisk until smooth, about 2 minutes. Gradually whisk in milk and reserved 2/3 '
             'cup vegetable cooking liquid. Whisk constantly over medium heat until sauce '
             'thickens and boils, about 3 minutes. Stir in spinach and cheese.\nUsing fingers, '
             'coarsely crumble cauliflower and broccoli in bowl. Add spinach béchamel sauce; '
             'stir to blend. Season with salt and pepper. Butter 1 1/2-quart baking dish. Spread '
             'vegetable mixture in prepared dish. (Can be made 6 hours ahead. Cover and '
             'chill.)\nPreheat oven to 350°F. Bake flan until puffed and heated through, about '
             '25 minutes if at room temperature and 35 minutes if chilled. Serve hot.',
             "['2 1/2 cups cauliflower florets', '2 1/2 cups broccoli florets', '2 6-ounce bags "
             "baby spinach leaves', '6 tablespoons (3/4 stick) butter', '1/4 cup all purpose "
             "flour', '2/3 cup whole milk', '2/3 cup freshly grated Parmesan cheese']")]


        response = self.app.post('/handle_ingredient_search',
                                 data={'include_ingredients': "cheese,broccoli",
                                        'exclude_ingredients': "garlic"})

        self.assertIn(
            b"Mac and Cheese with Chicken and Broccoli",
            response.data, "Should match")

    def test_display_recipe_route(self):
        '''Test the display recipe route.'''
        self.ds.cursor.fetchone.return_value = (789,
            'Cavatappi with Broccolini, Brown Butter, and Sage',
             'Bring a large pot of water to a boil. Fill a large bowl with water and ice '
             'and set aside.\nAdd 1 tablespoon kosher salt and the broccolini to the '
             'boiling water and cook until crisp-tender, 2 to 3 minutes. Using a spider '
             'or slotted spoon, transfer the Broccolini to the ice water to stop the '
             'cooking and let cool. Keep the pot of water boiling for the pasta. Drain '
             'the broccolini in a colander, cut the stalks in half crosswise, and set '
             'aside.\nIn a large nonstick skillet over medium heat, heat the olive oil '
             'until shimmering. Add the garlic and red pepper flakes and cook, stirring '
             'frequently, for 1 minute. Add the blanched broccolini, 1/2 teaspoon salt, '
             'and 1/4 teaspoon black pepper and sauté until tender, 3 to 5 minutes. '
             'Transfer the broccolini to a medium bowl and set aside.\nAdd the pasta '
             'to the boiling water and cook until al dente, about 2 minutes less than the '
             'directions on the package. Reserve 1/2 cup of the pasta water and drain the '
             'pasta in a colander.\nMeanwhile, wipe out the skillet, return it to '
             'medium-low heat, and add the butter. When the butter has melted, add the sage '
             'leaves and cook until the butter turns amber brown and the sage shrivels, 4 '
             'to 6 minutes. Add 1/4 teaspoon salt and black pepper. Stir in the cooked pasta '
             'until incorporated, then fold in the broccolini and 2 to 3 tablespoons of the '
             'reserved pasta water.\nStir in the Parmesan cheese, adding more pasta water until '
             'you achieve desired creaminess. Season with salt and pepper and serve hot.',
             "['Kosher salt', '2 bunches Broccolini (about 1 pound), ends trimmed, split "
             "lengthwise into halves or thirds depending on the thickness (or substitute "
             "broccoli rabe or broccoli)', '2 tablespoons extra-virgin olive oil', '2 large cloves "
             "garlic, minced', '1/4 teaspoon crushed red pepper flakes', 'Freshly ground black "
             "pepper', '1 pound cavatappi pasta (or your favorite ribbed pasta)', '6 tablespoons "
             "unsalted butter, cubed', '15 fresh sage leaves, torn', '1/2 cup freshly grated "
             "Parmesan cheese']")

        response = self.app.get('/display_recipe/789')
        self.assertIn(b"Cavatappi with Broccolini, Brown Butter, and Sage",
                      response.data, "Should match")

    def test_invalid_input(self):
        '''Test the random recipes route with invalid input.'''
        response = self.app.get('/random/abc', follow_redirects=True)
        self.assertIn(b"Oops! That page doesn\'t exist.",
                      response.data)

        response = self.app.get('/random/-1', follow_redirects=True)
        self.assertIn(b"Oops! That page doesn\'t exist.",
                      response.data)
