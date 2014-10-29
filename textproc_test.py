#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Adrian Chen
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_init(self):
		text = "tesing123"
		p = textproc.Processor(text)
		self.assertEqual(p.text, text, "'text' does not match input")

# Add Your Test Cases Here...
	def test_non_string(self):
		num = "4"	
		p = textproc.Processor(num)
		self.assertRaises(textproc.TextProcError)

	def test_count(self):
		p = textproc.Processor("hello")
		self.assertEqual(p.count(), 5, "'count' is incorrect")	
	
	def test_count_alpha(self):
		p = textproc.Processor("123hello123")
		self.assertEqual(p.count_alpha(), 5, "'count_alpha' is incorrect")	
		
	def test_count_numeric(self):
		p = textproc.Processor("123hello123")
		self.assertEqual(p.count_numeric(), 6, "'count_numeric' is incorrect")	

	def test_count_vowels(self):
		p = textproc.Processor("123hello123")
		self.assertEqual(p.count_vowels(), 2, "'count_vowels' is incorrect")	

	def is_phonenumber(self):
		p = textproc.Processor("222-333-4444")
		self.assertTrue(p.is_phonenumber(), "'is_phonenumber' is incorrect")	

# Main: Run Test Cases
if __name__ == '__main__':
	unittest.main()
