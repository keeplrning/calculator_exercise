import unittest
from src.calculator import calculate_pre

class TestCalulator(unittest.TestCase) :
    
    def test_calculator(self) :
        expression = '3'
        self.assertEqual(calculate_pre(expression), 3, 'Failed for expression "{}"'.format(expression))
        # expression = '+ 1 2'
        # self.assertEqual(calculate_pre(expression), 3, 'Failed for expression "{}"'.format(expression))
        # expression = '+ 1 * 2 3'
        # self.assertEqual(calculate_pre(expression), 7, 'Failed for expression "{}"'.format(expression))
        # expression = '+ * 1 2 3'
        # self.assertEqual(calculate_pre(expression), 5, 'Failed for expression "{}"'.format(expression))
        # expression = '- / 10 + 1 1 * 1 2'
        # self.assertEqual(calculate_pre(expression), 3, 'Failed for expression "{}"'.format(expression))
        # expression = '- 0 3'
        # self.assertEqual(calculate_pre(expression), -3, 'Failed for expression "{}"'.format(expression))
        # expression = '/ 3 2'
        # self.assertEqual(calculate_pre(expression), 1, 'Failed for expression "{}"'.format(expression))

