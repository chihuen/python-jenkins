
from project.add import add
from unittest import TestCase

class StandAloneTests(TestCase):
	"""Test the stand-alone module functuons."""

	def test_add(self):
		self.assertEqual(add(1, 1), 2)

	def test_add_param_is_str(self):
		self.assertRaises(TypeError, add('1', 2))
		self.assertRaises(TypeError, add(1, '1'))
		self.assertRaises(TypeError, add('1', '2'))
