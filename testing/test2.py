import unittest
import guess

class TestGuess(unittest.TestCase):
	def test_inserted_num(self):
		result = guess.inserted_num(5, 5)
		self.assertTrue(result)

	def test_inserted_num2(self):
		result = guess.inserted_num(2, 4)
		self.assertFalse(result)

	def test_inserted_num3(self):
		result = guess.inserted_num(2, 'hi')
		self.assertFalse(result)

	

if __name__ == "__main__":
	unittest.main()
