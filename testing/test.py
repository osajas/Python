import unittest
import main

class TestDoStuff(unittest.TestCase):
	def test_do_stuff(self):
		result = main.do_stuff(5) + 5
		self.assertEqual(result, 15)


	def test_do_stuff2(self):
		test = "hi"
		result = main.do_stuff("hi")
		self.assertTrue(isinstance(result, ValueError))

	def test_do_stuff3(self):
		test = None
		result = main.do_stuff(test)
		self.assertEqual(result, "Please inset a number")

	def test_do_stuff4(self):
		test = 0
		result = main.do_stuff(test)
		self.assertEqual(result, 5)

if __name__ == "__main__":
	unittest.main()

