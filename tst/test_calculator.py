import unittest
from src.calculator import calculate_pre, calculate_infix


class TestCalulator(unittest.TestCase):
    
    def test_calculator_pre(self):
        expression = '3'
        self.assertEqual(calculate_pre(expression), 3, 'Failed for expression "{}"'.format(expression))
        expression = '+ 1 2'
        self.assertEqual(calculate_pre(expression), 3, 'Failed for expression "{}"'.format(expression))
        expression = '+ 1 * 2 3'
        self.assertEqual(calculate_pre(expression), 7, 'Failed for expression "{}"'.format(expression))
        expression = '+ * 1 2 3'
        self.assertEqual(calculate_pre(expression), 5, 'Failed for expression "{}"'.format(expression))
        expression = '- / 10 + 1 1 * 1 2'
        self.assertEqual(calculate_pre(expression), 3, 'Failed for expression "{}"'.format(expression))
        expression = '- 0 3'
        self.assertEqual(calculate_pre(expression), -3, 'Failed for expression "{}"'.format(expression))
        expression = '/ 3 2'
        self.assertEqual(calculate_pre(expression), 1.5, 'Failed for expression "{}"'.format(expression))

    def test_calculator_infix(self):
        expression = '( 1 + 2 )'
        self.assertEqual(calculate_infix(expression), 3, 'Failed for expression "{}"'.format(expression))
        expression = '( 1 + ( 2 * 3 ) )'
        self.assertEqual(calculate_infix(expression), 7, 'Failed for expression "{}"'.format(expression))
        expression = '( ( 1 * 2 ) + 3 )'
        self.assertEqual(calculate_infix(expression), 5, 'Failed for expression "{}"'.format(expression))
        expression = '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )'
        self.assertEqual(calculate_infix(expression), -1.8, 'Failed for expression "{}"'.format(expression))
