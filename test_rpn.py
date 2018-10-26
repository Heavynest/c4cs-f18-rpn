import unittest
import run

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = run.calculate('1 1 +')
		self.assertEqual(2,result)
	def test_sub(self):
		result = run.calculate('4 3 -')
		self.assertEqual(1,result)
	def test_multiple(self):
		result=run.calculate('2 5 *')
		self.assertEqual(10,result)
	def test_division(self):
		result=run.calculate('12 4 /')
		self.assertEqual(3,result)
