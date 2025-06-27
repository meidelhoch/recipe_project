'''
Contains tests for the command line interface of the program.
'''

import unittest
from unittest.mock import MagicMock, patch
import sys
from io import StringIO
from cl import main
from ProductionCode.datasource import DataSource



class TestMainFunction(unittest.TestCase):
    '''
    Tests the main interface.
    '''
    @patch('ProductionCode.datasource.psycopg2.connect')
    def setUp(self, mock_connect):
        '''
        Sets up the test environment by mocking the get_data function.
        '''
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        mock_connect.return_value = self.mock_conn
        self.ds = DataSource()

    def test_main_random(self):
        '''Tests the main function for getting random recipes'''

        self.ds.cursor.fetchall.return_value = [(11286,
                             'Chocolate and Peppermint Candy Ice Cream Sandwiches',
                             'Stir together ice cream...',
                             "['1 pint superpremium vanilla ice cream...']")]

        sys.argv = ['cl.py', '--random', '1']
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertIn('Chocolate and Peppermint Candy Ice Cream Sandwiches', output)

    def test_command_line_search(self):
        '''
        Tests the command line interface.
        '''
        self.ds.cursor.fetchall.return_value = [(13401, 'Thai-Style Chicken and Rice Soup',
        'Combine stock, water, curry paste, garlic, ginger, ...',
        "['8 cups chicken stock or low-sodium chicken broth (64 fl oz)...']")]

        # Test the command line interface with the --include option
        sys.argv = ['cl.py', '--search',
                    '--include_ingredients', 'chicken, rice']
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertIn('Thai-Style Chicken and Rice Soup', output, "Should be the same")

        self.ds.cursor.fetchall.return_value = [(13483, 'White Chicken Chili',
        'In a large kettle soak beans in cold water to cover...',
        "['1/2 pound dried navy beans, picked over...']")]

        # Test the command line interface with both --incluce and --omit option
        sys.argv = ['cl.py', '--search', '--include_ingredients',
                    'chicken', '--omit_ingredients', 'kale']
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertIn('White Chicken Chili', output, "Should be the same")

    def test_command_line_omit(self):
        '''
        Tests the command line interface with omitted ingredients.
        '''
        self.ds.cursor.fetchall.return_value = [(13499, 'Spanakopita',
        'Melt 1 tablespoon butter in a 12-inch heavy skillet...',
        "['1 stick (1/2 cup) plus 1 tablespoon unsalted butter...']")]

        # Test the command line interface with --omit option
        sys.argv = ['cl.py', '--search', '--omit_ingredients', 'chicken']
        sys.stdout = StringIO()

        main()

        output = sys.stdout.getvalue().strip()
        self.assertIn('Spanakopita', output, "Should be the same")

    def test_command_line_help(self):
        '''
        Tests the command line interface with help option.
        '''

        # Test the command line interface with the --help option
        sys.argv = ['cl.py', '--help']
        sys.stdout = StringIO()

        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 0, "Exit code should be 0")

        expected_output = "usage: cl.py [-h] (-s | -r n)"
        expected_output = expected_output.strip()

        output = sys.stdout.getvalue().strip()
        self.assertIn(expected_output, output, "Should be the same")


if __name__ == "__main__":
    unittest.main()
