import unittest
from postcodesuk import *

class TestPostCodesUk(unittest.TestCase):

	# starts with two letters, one number, one letter
	def test_correct_post_codes_uk_211(self):
		self.assertEqual(format_and_validate_post_codes_uk("aa9c 9aa"), 'AA9C 9AA')

	# starts with two letters, one number
	def test_correct_post_codes_uk_21(self):
		self.assertEqual(format_and_validate_post_codes_uk("aa9 9AA"), 'AA9 9AA')

	# starts with two letters, two numbers
	def test_correct_post_codes_uk_22(self):
		self.assertEqual(format_and_validate_post_codes_uk("aa99 9aa"), 'AA99 9AA')

	# starts with one letter, one number, one letter
	def test_correct_post_codes_uk_111(self):
		self.assertEqual(format_and_validate_post_codes_uk("a9a 9aa"), 'A9A 9AA')

	# starts with one letter, one number
	def test_correct_post_codes_uk_11(self):
		self.assertEqual(format_and_validate_post_codes_uk("a9 9aa"), 'A9 9AA')

	# starts with one letter, two numbers
	def test_correct_post_codes_uk_12(self):
		self.assertEqual(format_and_validate_post_codes_uk("a99 9aa"), 'A99 9AA')

